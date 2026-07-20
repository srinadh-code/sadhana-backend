from django.db import models
from cloudinary.models import CloudinaryField


class AdmissionHero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    # button_text = models.CharField(max_length=50, default="Apply Now")
    # image = CloudinaryField("image")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Admission Hero"
        verbose_name_plural = "Admission Hero"

    def __str__(self):
        return self.title


class Eligibility(models.Model):
    title = models.CharField(max_length=300)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Eligibility"
        verbose_name_plural = "Eligibility"

    def __str__(self):
        return self.title


class RequiredDocument(models.Model):
    title = models.CharField(max_length=300)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Required Document"
        verbose_name_plural = "Required Documents"

    def __str__(self):
        return self.title


class AdmissionEnquiry(models.Model):

    STATUS_CHOICES = (
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Admission Confirmed", "Admission Confirmed"),
        ("Rejected", "Rejected"),
    )

    student_name = models.CharField(max_length=150)
    parent_name = models.CharField(max_length=150)

    email = models.EmailField()
    phone = models.CharField(max_length=15)

    grade = models.CharField(max_length=100)

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="New"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Admission Enquiry"
        verbose_name_plural = "Admission Enquiries"

    def __str__(self):
        return f"{self.student_name} ({self.grade})"


class FAQ(models.Model):
    question = models.CharField(max_length=250, unique=True)
    answer = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question