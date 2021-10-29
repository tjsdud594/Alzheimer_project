from django import forms
from .models import PredData

class UploadForm(forms.Form):
    upimg = forms.ImageField()

    class Meta:
        managed = False
        model = PredData # Form 필드를 만들때  참조/save()시 데이터를 저장할 Model클래스 지정.
