from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    message=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.email
    class Meta:
        db_table="feedback"

class Location(models.Model):
    state=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    locality=models.CharField(max_length=100,blank=True,null=True)
    cate=models.CharField(max_length=100,blank=True,null=True)
    subcate=models.CharField(max_length=100,blank=True,null=True)
    location_title=models.CharField(max_length=100,blank=True,null=True)
    des=models.CharField(max_length=100,blank=True,null=True)
    img1=models.ImageField(upload_to='images/')
    img2=models.ImageField(upload_to='images/')
    img3=models.ImageField(upload_to='images/')
    img4=models.ImageField(upload_to='images/')
    v_status=models.IntegerField(blank=True,null=True)
    info=models.CharField(max_length=100,blank=True,null=True)
    vid=models.IntegerField(blank=True,null=True)
    map=models.CharField(max_length=10000,blank=True,null=True)
    def __str(self):
        return self.location_title
    class Meta:
        db_table="loaction"

class Payment(models.Model):
    uid=models.IntegerField(null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    loc_id=models.IntegerField(null=True,blank=True)
    info=models.CharField(max_length=100,blank=True,null=True)
