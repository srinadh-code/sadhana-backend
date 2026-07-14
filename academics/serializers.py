from rest_framework import serializers
from .models import (
    AcademicHero,
    AcademicProgram,
    TeachingMethod,
    Department,
    AcademicCalendar,
    AcademicDownload,
)


class AcademicHeroSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AcademicHero
        fields = [
            "id",
            "title",
            "subtitle",
            "image",
            "image_url",
            "is_active",
            "updated_at",
        ]

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class AcademicProgramSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AcademicProgram
        fields = [
            "id",
            "level",
            "grades",
            "description",
            "image",
            "image_url",
            "display_order",
            "is_active",
            "created_at",
            "updated_at",
        ]

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class TeachingMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachingMethod
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "display_order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "display_order",
            "is_active",
            "created_at",
        ]


class AcademicCalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicCalendar
        fields = [
            "id",
            "month",
            "event",
            "display_order",
            "is_active",
            "created_at",
        ]


class AcademicDownloadSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = AcademicDownload
        fields = [
            "id",
            "title",
            "file",
            "file_url",
            "display_order",
            "is_active",
            "created_at",
        ]

    def get_file_url(self, obj):
        return obj.file.url if obj.file else None