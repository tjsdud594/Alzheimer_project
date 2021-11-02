import os
import json
import numpy as np
# from PIL import Image
import PIL.Image as PILI 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Backend import settings
from . import forms
from .apps import FunctionConfig
from .models import PredData
from django.shortcuts import render
import cv2
import boto3
import urllib.request
import time
import sys
import hashlib
import base64

@csrf_exempt # form post 요청을 받을 때 csrf 토큰없이 요청할 수 있도록 처리.
def predict(request):
    # 요청파라미터 - text: request.POST, file: request.FILES
    form = forms.UploadForm(request.POST, request.FILES)
    if form.is_valid(): #요청파라미터 검증. True: 검증 성공, False: 검증 실패
        clean_data = form.cleaned_data #Form에서 직접 값을 조회할 수 없다. form.cleaned_data: 검증을 통과한 
                                       #요청파라미터들을 딕셔너리로 반환. 이 딕셔너리를 이용해 조회
        img_field  = clean_data['upimg'] #업로드된 파일을 조회
        print(img_field, type(img_field))
        
         # aws로 upload
        AWS_ACCESS_KEY_ID = "AKIA3MDEZOF62YYMEL5K"
        AWS_SECRET_ACCESS_KEY = "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"
        AWS_S3 = "s3"
        S3_BUCKET_NAME = "alzheimer-django"

        # Making AWS Session
        session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


        # create Key => timestamp
        time_str = str(time.time())
        time_str = "img_" + time_str.replace(".","") + ".png"

        s3_client = boto3.client(
		AWS_S3,
		aws_access_key_id=AWS_ACCESS_KEY_ID,
		aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
	    )

        s3_client.upload_fileobj(
                img_field,
                S3_BUCKET_NAME,
                time_str,
                ExtraArgs={
                    "ContentType": "image/png",
                    'ACL' : 'public-read',
                }
        )

        # aws 연결결과 확인
        # aws_result = s3_client.upload_fileobj.get('ResponseMetadata')
        # if aws_result.get('HTTPStatusCode') == 200:
        #     print('File Uploaded Successfully')
        # else:
        #     print('File Not Uploaded')
        #     return {
        #     'Response' :  
        #         {
        #             'Message': 'File Not Uploaded', 
        #             'Result' : 'Error',
        #             'Details': 'Error occured while uploading masking image'
        #         }
        #     }

        # aws에서 img download
        path_img = "https://alzheimer-django.s3.us-east-1.amazonaws.com/" + time_str
        print(path_img)
        TEMP_IMG_NAME = "media/img.png"

        time.sleep(2)

        # download 이미지 저장
        urllib.request.urlretrieve(path_img, TEMP_IMG_NAME)


        image = PILI.open(TEMP_IMG_NAME).convert('RGB') # 이미지 로딩
        # print(image.size)

        image_resize = image.resize((208,176)) 
        
        image_arr = np.array(image_resize) #PIL 이미지 타입을 ndarray 변환

        image_c = image_arr.copy()

        image_arr = image_c/255. # 정규화

        input_tensor = image_arr[np.newaxis, ...] # 임시모델 말고 개량모델 완성시 해당 코드 변경 필요!

        model = FunctionConfig.model
        pred = model.predict(input_tensor) #출력층 activation: softmax 
        cls = pred

        # aws s3에 이미지를 저장할 것이므로 해당 코드 주석처리
        # save_path = os.path.join(settings.MEDIA_ROOT, img_field.name)
        # print(save_path)
        # image.save(save_path) #PIL Image객체.save(경로) : 이미지 저장.

        result = {
                'result':str(cls),
                'mild': float(pred[0,0]),
                'moderate' : float(pred[0,1]),
                'normal' : float(pred[0,2]),
                'very_mild' : float(pred[0,3]),
                'img_url' : path_img  
                }


        try :
            test = PredData(
                            result = result['result'], 
                            mild = result['mild'], 
                            moderate = result['moderate'], 
                            normal = result['normal'], 
                            very_mild = result['very_mild'],
                            img_url = result['img_url']
                            )
            test.save()
        except :
            test  = None

        return render(request, 'function/result.html', {'result' : test}) 
        # result_str = json.dumps(result)   #Dictionary 를 JSON 문자열로 변환.
    
        # return HttpResponse(result_str)

