from django.contrib import admin

from .models import (
    AdmissionHero,
    Eligibility,
    RequiredDocument,
    AdmissionEnquiry,
    FAQ,
)


@admin.register(AdmissionHero)
class AdmissionHeroAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
    )


@admin.register(Eligibility)
class EligibilityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "title",
    )


@admin.register(RequiredDocument)
class RequiredDocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "title",
    )


@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "parent_name",
        "grade",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "grade",
    )

    search_fields = (
        "student_name",
        "parent_name",
        "phone",
        "email",
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


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "question",
    )