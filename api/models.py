import os

from django.db import models
from django.dispatch import receiver


# Create your models here.


class UploadedImage(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# when user deletes the image it will automatically delete respective image file in the database
@receiver(models.signals.post_delete, sender=UploadedImage)
def auto_delete_img_on_delete(sender, instance, **kwargs):
    if instance.img:
        # if the path that we are providing is a file then we will remove it
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)
