from django.contrib import admin
from .models import (
    AcademicHero,
    AcademicProgram,
    TeachingMethod,
    Department,
    AcademicCalendar,
    AcademicDownload,
)


@admin.register(AcademicHero)
class AcademicHeroAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "updated_at")


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = (
        "level",
        "grades",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )


@admin.register(TeachingMethod)
class TeachingMethodAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )


@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = (
        "month",
        "event",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )


@admin.register(AcademicDownload)
class AcademicDownloadAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )