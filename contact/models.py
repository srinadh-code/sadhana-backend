# Create your models here.
from django.db import models


class ContactInfo(models.Model):
    school_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    office_hours = models.CharField(max_length=200)
    map_url = models.TextField(help_text="Google Maps Embed URL")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return self.school_name


class ContactEnquiry(models.Model):

    STATUS_CHOICES = (
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name