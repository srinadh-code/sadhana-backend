from rest_framework import serializers
from .models import Facility


# class FacilitySerializer(serializers.ModelSerializer):

#     desc = serializers.CharField(source="description", read_only=True)

#     class Meta:
#         model = Facility
#         fields = [
#             "id",
#             "title",
#             "description",
#             "desc",
#             "icon",
#             "image",
#             "is_active",
#         ]

#     def to_representation(self, instance):
#         data = super().to_representation(instance)

#         request = self.context.get("request")

#         if request and instance.image:
#             data["image"] = request.build_absolute_uri(instance.image.url)

#         return data




class FacilitySerializer(serializers.ModelSerializer):

    desc = serializers.CharField(source="description", read_only=True)

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Facility
        fields = [
            "id",
            "title",
            "description",
            "desc",
            "icon",
            "image",
            "image_url",
            "is_active",
        ]

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None