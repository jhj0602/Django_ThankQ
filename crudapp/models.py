from django.db import models
from django.contrib.auth.models import User
#외부모델 User을 활용하기위해 임포트하기. 

class Blog(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    images = models.ImageField(blank=True, upload_to="images", null=True)
    qr_img = models.ImageField(blank=True, upload_to="qr_img", null=True)#qrcode
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


# class imange(models.Model):
#     qr_img = models.ImageField(blank=True, null=True)#qrcode

