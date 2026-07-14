from django.db import models

# Create your models here.
from django.db import models

from cloudinary.models import CloudinaryField
class Gallery(models.Model):
    CATEGORY_CHOICES = (
        ("Campus", "Campus"),
        ("Classrooms", "Classrooms"),
        ("Laboratories", "Laboratories"),
        ("Sports", "Sports"),
        ("Events", "Events"),
        ("Transport", "Transport"),
        ("Hostel", "Hostel"),
        ("Activities", "Activities"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Campus",
    )

    image = CloudinaryField("image")

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.title
    