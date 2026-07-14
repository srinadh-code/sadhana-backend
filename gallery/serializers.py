from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "category",
            "description",
            "display_order",
            "is_active",
            "image",
            "image_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must contain at least 3 characters."
            )
        return value