from django.db import models

# class Test(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

class PredData(models.Model) :
    result = models.CharField(max_length = 50)
    normal = models.FloatField()
    very_mild =  models.FloatField()
    mild= models.FloatField()
    moderate =  models.FloatField()

    def __str__(self) :
        return self.result