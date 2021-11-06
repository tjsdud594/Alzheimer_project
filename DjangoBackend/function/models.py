from django.db import models
from django.db.models.fields.related import ForeignKey
from account.models import CustomUser

# class Test(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

class PredData(models.Model) :
    create_at = models.DateTimeField(verbose_name="검사일시", auto_now_add=True)
    email = models.ForeignKey('account.CustomUser',
                                on_delete=models.CASCADE)
    normal = models.FloatField()
    very_mild =  models.FloatField()
    mild= models.FloatField()
    moderate =  models.FloatField()
    img_url = models.CharField(max_length = 300)
    img_name = models.CharField(max_length = 300)

    def __str__(self) :
        return f"No.{self.pk}/생성날짜.{self.create_at}/email.{self.email}"

    class Meta:
        ordering = ['-create_at']