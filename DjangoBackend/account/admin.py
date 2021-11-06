from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


# class CustomerUserAdmin(UserAdmin):
#     # class 변수를 변경
#     # 사용자 수정화면의 **기본정보**카테고리에 나올 Model Field들을 선언
#     UserAdmin.fieldsets[1][1]['fields'] = ('username', 'email', 'hospital')

#     # 사용자 목록 화면에 나올 Field들을 정의
#     list_display = ['username', 'email', 'hospital']

# admin.site.register(CustomUser, CustomerUserAdmin)
admin.site.register(CustomUser)