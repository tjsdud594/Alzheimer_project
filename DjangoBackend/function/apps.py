from django.apps import AppConfig
from tensorflow.keras import models


class FunctionConfig(AppConfig):
    name = 'function'
    model = models.load_model(r'.\model\alzheimer_project')

