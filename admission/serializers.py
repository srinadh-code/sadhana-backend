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
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title is required.")
        return value

    def validate_subtitle(self, value):
        if not value.strip():
            raise serializers.ValidationError("Subtitle is required.")
        return value        
        


    



class EligibilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Eligibility
        fields = [
            "id",
            "title",
            "display_order",
            "is_active",
        ]
    def validate_title(self, value):
        if not value.strip():
                raise serializers.ValidationError(
                "Eligibility is required."
            )
        return value

    def validate_display_order(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Display Order cannot be negative."
            )
        return value
class RequiredDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequiredDocument
        fields = [
            "id",
            "title",
            "display_order",
            "is_active",
        ]
    def validate_display_order(self, value):
        if value < 0:
                raise serializers.ValidationError(
            "Display Order cannot be negative."
            )
        return value

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
    def validate_question(self, value):
            if not value.strip():
                raise serializers.ValidationError(
                "Question is required."
            )
            return value

    def validate_answer(self, value):
        if not value.strip():
                raise serializers.ValidationError(
                "Answer is required."
            )
        return value

    def validate_display_order(self, value):
            if value < 0:
                raise serializers.ValidationError(
                "Display Order cannot be negative."
            )
            return value
