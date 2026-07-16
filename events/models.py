from django.db import models
from cloudinary.models import CloudinaryField


class EventCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Event Category"
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.name


class Event(models.Model):

    category = models.ForeignKey(
        EventCategory,
        on_delete=models.CASCADE,
        related_name="events",
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = CloudinaryField("image")

    event_date = models.DateField()

    event_time = models.TimeField(
        blank=True,
        null=True,
    )

    venue = models.CharField(
        max_length=200,
        blank=True,
    )

    upcoming = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "display_order",
            "-event_date",
        ]

    def __str__(self):
        return self.title