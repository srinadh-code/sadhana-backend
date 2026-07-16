from rest_framework import serializers

from .models import (
    EventCategory,
    Event,
)


# =====================================================
# EVENT CATEGORY
# =====================================================

class EventCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EventCategory
        fields = "__all__"


# =====================================================
# EVENT
# =====================================================

class EventSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_image_url(self, obj):

        if obj.image:
            return obj.image.url

        return None