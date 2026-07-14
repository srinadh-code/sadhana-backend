from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class HostelInfo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = models.TextField()
    image = CloudinaryField("image")
    

from cloudinary.models import CloudinaryField


class HostelRoom(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField("image")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)






class HostelFacility(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class HostelRule(models.Model):
    rule = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.rule[:50]


class HostelEnquiry(models.Model):
    parent_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    child_class = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent_name