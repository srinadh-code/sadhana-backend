from rest_framework import serializers
from .models import ContactInfo, ContactEnquiry


class ContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactInfo
        fields = "__all__"


class ContactEnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEnquiry
        fields = "__all__"
        read_only_fields = (
            "status",
            "created_at",
        )

    def validate_full_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Name must contain at least 3 characters."
            )
        return value

    def validate_subject(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Subject is too short."
            )
        return value

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Message must contain at least 10 characters."
            )
        return value