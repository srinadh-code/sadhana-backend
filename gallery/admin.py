from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "display_order",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-created_at",
    )