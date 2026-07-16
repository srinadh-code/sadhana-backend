from django.db import models
from cloudinary.models import CloudinaryField


class HeroSlide(models.Model):
    badge = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = CloudinaryField("image")

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title


class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True)

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.value}{self.suffix} {self.label}"


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        help_text="Lucide icon name (GraduationCap, Users, Trophy, BookOpen, etc.)"
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title


class CallToAction(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)

    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255)

    background_image = CloudinaryField("image")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to="testimonials/")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name