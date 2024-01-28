from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Dob=models.CharField(max_length=20,default="")
    Phno=models.IntegerField(default=0)
    Email=models.CharField(max_length=50,default="")
    Password=models.CharField(max_length=50,default="")
    Conpass=models.CharField(max_length=50,default="")
 