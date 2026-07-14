from rest_framework import serializers
from .models import About, Faculty, Timeline, Achievement


class AboutSerializer(serializers.ModelSerializer):
    hero_image_url = serializers.SerializerMethodField()
    story_image_url = serializers.SerializerMethodField()
    principal_image_url = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = "__all__"

    def get_hero_image_url(self, obj):
        return obj.hero_image.url if obj.hero_image else None

    def get_story_image_url(self, obj):
        return obj.story_image.url if obj.story_image else None

    def get_principal_image_url(self, obj):
        return obj.principal_image.url if obj.principal_image else None


class FacultySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"