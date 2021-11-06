from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'function'

urlpatterns = [
    # path('request', TemplateView.as_view(template_name='function/request.html'), name='request'),
    path('upload', TemplateView.as_view(template_name='function/upload.html'), name='upload'),
    # path('predict', views.predict, name='predict'),
    path('predict', views.predict, name='predict'),
    path('', TemplateView),
]