from django.db import models
from cloudinary.models import CloudinaryField


class AcademicHero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    image = CloudinaryField("image")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Academic Hero"
        verbose_name_plural = "Academic Hero"

    def __str__(self):
        return self.title


class AcademicProgram(models.Model):
    level = models.CharField(max_length=200)
    grades = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField("image")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.level


class TeachingMethod(models.Model):
    ICON_CHOICES = [
        ("Lightbulb", "Lightbulb"),
        ("Users", "Users"),
        ("BookOpen", "BookOpen"),
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=200)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name


class AcademicCalendar(models.Model):
    month = models.CharField(max_length=100)
    event = models.CharField(max_length=300)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.month} - {self.event}"


class AcademicDownload(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField(resource_type="raw")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title