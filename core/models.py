from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Submit(models.Model):
    name=models.CharField(max_length=300)
    gender_chioces=[('m','Male' ) ,  ('f' , "Female")]
    department=models.CharField(max_length=300)
    faculty=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    description_of_item=models.TextField()
    profile_pic=models.ImageField(upload_to="writers_pics")
    status=models.CharField( blank=True , null=True ,choices=[('Lost', 'Lost'),('Found', 'Found')])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    item_name=models.CharField(max_length=300 ,blank=True ,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    


