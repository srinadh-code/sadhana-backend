from rest_framework import serializers
from .models import (
    HostelInfo,
    HostelRoom,
    HostelFacility,
    HostelRule,
    HostelEnquiry,
)

from rest_framework import serializers
from .models import HostelInfo , HostelRoom


class HostelInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HostelInfo
        fields = [
            "id",
            "title",
            "subtitle",
            "description",
            "image",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get("request")

        if instance.image:
            data["image"] = request.build_absolute_uri(instance.image.url)
        else:
            data["image"] = None

        return data




# class HostelRoomSerializer(serializers.ModelSerializer):

#     image = serializers.ImageField(required=False)

#     class Meta:
#         model = HostelRoom
#         fields = [
#             "id",
#             "title",
#             "description",
#             "price",
#             "image",
#             "display_order",
#             "is_active",
#         ]

#     def to_representation(self, instance):

#         data = super().to_representation(instance)

        # if instance.image:
        #     data["image"] = instance.image.url
        # else:
        #     data["image"] = None

        # return data



from rest_framework import serializers
from .models import HostelRoom


class HostelRoomSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = HostelRoom
        fields = [
            "id",
            "title",
            "description",
            "price",
            "image",
            "image_url",
            "display_order",
            "is_active",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")

        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url

        return None

class HostelFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = HostelFacility
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "display_order",
            "is_active",
        ]


class HostelRuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = HostelRule
        fields = [
            "id",
            "rule",
            "display_order",
            "is_active",
        ]


class HostelEnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = HostelEnquiry
        fields = [
            "id",
            "parent_name",
            "phone",
            "child_class",
            "message",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]