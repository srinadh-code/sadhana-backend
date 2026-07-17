from rest_framework import serializers

from .models import (
    AdmissionHero,
    Eligibility,
    RequiredDocument,
    AdmissionEnquiry,
    FAQ,
)

class AdmissionHeroSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = AdmissionHero
        fields = [
            "id",
            "title",
            "subtitle",
            # "button_text",
            # "image",
            # "image_url",
            "is_active",
        ]

    



class EligibilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Eligibility
        fields = [
            "id",
            "title",
            "display_order",
            "is_active",
        ]
class RequiredDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequiredDocument
        fields = [
            "id",
            "title",
            "display_order",
            "is_active",
        ]

class AdmissionEnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdmissionEnquiry
        fields = [
            "id",
            "student_name",
            "parent_name",
            "email",
            "phone",
            "grade",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = (
            "status",
            "created_at",
        )

    def validate_phone(self, value):

        value = value.strip()

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number should contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be 10 digits."
            )

        return value
    

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = [
            "id",
            "question",
            "answer",
            "display_order",
            "is_active",
        ]