from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class CustomUser(AbstractUser):
# class User(AbstractUser):
    
    # 추가할 Model Field들을 정의

    # EmailField: CharField(varchar) + 이메일형식 검증이 추가(@)
    # email = models.EmailField(max_length=100, primary_key=True, verbose_name='이메일')

    name = models.CharField(max_length=100, verbose_name='이름', default='Jhon Doe', null=False)

    # password1 = models.CharField(max_length=300, verbose_name='비밀번호1')

    # password2 = models.CharField(max_length=300, verbose_name='비밀번호2')

    hospital = models.CharField(max_length=100, verbose_name='병원', null=False)

    agreement1 = models.BooleanField(default=False)

    agreement2 = models.BooleanField(default=False)

    agreement3 = models.BooleanField(default=False)

    def __str__(self):
        return self.email

CustomUser = get_user_model()

