from django.contrib import admin
from .models import ContactInfo, ContactEnquiry


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "school_name",
        "phone",
        "email",
        "whatsapp",
    )


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "subject",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "subject",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )