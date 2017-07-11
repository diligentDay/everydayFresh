from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=50)
    gpic=models.ImageField(upload_to='goods')
    gprice=models.DecimalField(max_digits=5,decimal_places=2)#999.99
    gclick = models.IntegerField(default=0)
    gunit=models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    gsubtitle=models.CharField(max_length=200)
    gkucun = models.IntegerField(default=100)
    gcontent=HTMLField()
    gtype=models.ForeignKey('TypeInfo')