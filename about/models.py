from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    # Hero
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    hero_image = CloudinaryField("image")

    # Story
    story_section_title = models.CharField(max_length=100, default="Our Story")
    story_heading = models.CharField(max_length=255)
    story_description_one = models.TextField()
    story_description_two = models.TextField(blank=True)
    story_image = CloudinaryField("image")

    # Vision / Mission / Values
    vision = models.TextField()
    mission = models.TextField()
    values = models.TextField()

    # Principal
    principal_name = models.CharField(max_length=150)
    principal_designation = models.CharField(
        max_length=100,
        default="Principal"
    )
    principal_quote = models.CharField(max_length=255)
    principal_message = models.TextField()
    principal_image = CloudinaryField("image")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return "About Page"


class Faculty(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(
        help_text="Experience in Years"
    )

    image = CloudinaryField("image")

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name


class Timeline(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.year} - {self.title}"


class Achievement(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.year} - {self.title}"