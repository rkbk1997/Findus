from django.db import models

# Create your models here.
class Cate(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)
    pic=models.ImageField(upload_to='images/')
    def __str__(self):
            return self.name
    class Meta:
        db_table="cate"


class Subcate(models.Model):
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    nameofsubcate = models.CharField(max_length=100)
    def __str__(self):
            return self.nameofsubcate
    class Meta:
        db_table="subcate"

class Notification(models.Model):
        date=models.CharField(max_length=100,blank=True,null=True)
        des=models.CharField(max_length=1000,blank=True,null=True)
        def __str__(self):
                return self.des
        class Meta:
                db_table="notification"