import os
import json
import numpy as np
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Backend import settings
from . import forms
from .apps import FunctionConfig
from .models import PredData
from django.shortcuts import render
import cv2

@csrf_exempt # form post 요청을 받을 때 csrf 토큰없이 요청할 수 있도록 처리.
def predict(request):
    # 요청파라미터 - text: request.POST, file: request.FILES
    form = forms.UploadForm(request.POST, request.FILES)
    if form.is_valid(): #요청파라미터 검증. True: 검증 성공, False: 검증 실패
        clean_data = form.cleaned_data #Form에서 직접 값을 조회할 수 없다. form.cleaned_data: 검증을 통과한 
                                       #요청파라미터들을 딕셔너리로 반환. 이 딕셔너리를 이용해 조회
        img_field  = clean_data['upimg'] #업로드된 파일을 조회
        print(img_field, type(img_field))
        
        image = Image.open(img_field) # 이미지 로딩

        image_resize = image.resize((208,176)) 
        
        image_arr = np.array(image_resize) #PIL 이미지 타입을 ndarray 변환

        image_c = image_arr.copy()
        image_color = cv2.cvtColor(image_c, cv2.COLOR_GRAY2RGB)

        image_arr = image_color/255. # 정규화

        input_tensor = image_arr[np.newaxis, ...] # 임시모델 말고 개량모델 완성시 해당 코드 변경 필요!

        model = FunctionConfig.model
        pred = model.predict(input_tensor) #출력층 activation: softmax 
        cls = pred

        save_path = os.path.join(settings.MEDIA_ROOT, img_field.name)
        print(save_path)
        image.save(save_path) #PIL Image객체.save(경로) : 이미지 저장.

        result = {
                'result':str(cls),
                'mild': float(pred[0,0]),
                'moderate' : float(pred[0,1]),
                'normal' : float(pred[0,2]),
                'very_mild' : float(pred[0,3]),
                'img_url':"/media/{}".format(img_field.name)
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

        return render(request, 'function/response.html', result) 


