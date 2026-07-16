from rest_framework import serializers
from .models import HeroSlide, Statistic, WhyChooseUs, CallToAction,Testimonial


class HeroSlideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSlide
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"


class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = "__all__"


class CallToActionSerializer(serializers.ModelSerializer):
    background_image_url = serializers.SerializerMethodField()

    class Meta:
        model = CallToAction
        fields = "__all__"

    def get_background_image_url(self, obj):
        return obj.background_image.url if obj.background_image else None
    
class TestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else ""