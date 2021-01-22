from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class newcrud(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    id = models.IntegerField(max_length=5000, default="")
    # def __str__(self):
    #     return self.title
