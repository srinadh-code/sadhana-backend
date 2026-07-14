from django.contrib import admin

from .models import (
    About,
    Faculty,
    Timeline,
    Achievement,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        "hero_title",
        "principal_name",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "hero_title",
        "principal_name",
    )


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "subject",
        "experience",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "role",
        "subject",
    )

    ordering = (
        "display_order",
    )


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "year",
        "title",
    )

    ordering = (
        "display_order",
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "year",
        "title",
    )

    ordering = (
        "display_order",
    )