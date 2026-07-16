
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
        if obj.hero_image:
            return str(obj.hero_image.url)
        return None

    def get_story_image_url(self, obj):
        if obj.story_image:
            return str(obj.story_image.url)
        return None

    def get_principal_image_url(self, obj):
        if obj.principal_image:
            return str(obj.principal_image.url)
        return None


class FacultySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = "__all__"

    def get_image_url(self, obj):
        if obj.image:
            return str(obj.image.url)
        return None


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"