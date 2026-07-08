from django.db import models

class Event(models.Model):

    CATEGORY_CHOICES = (
        ("Academic","Academic"),
        ("Sports","Sports"),
        ("Cultural","Cultural"),
        ("National","National"),
        ("Festival","Festival"),
        ("Other","Other"),
    )

    title = models.CharField(max_length=250)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    event_date = models.DateField()

    image = models.ImageField(upload_to="events")

    is_upcoming = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-event_date"]

    def __str__(self):
        return self.title