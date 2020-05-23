from django.db import models

# Create your models here.
class Registration(models.Model):
    fname=models.CharField(max_length=100,blank=True,null=True)
    lname=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    gender=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=300,blank=True,null=True)
    status=models.IntegerField(blank=True,null=True)
    role=models.CharField(max_length=50,blank=True,null=True)
    info=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
            return self.username
    class Meta:
        db_table="registration"