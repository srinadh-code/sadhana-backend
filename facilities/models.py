from django.db import models
from cloudinary.models import CloudinaryField

class Facility(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    image = CloudinaryField("image")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title