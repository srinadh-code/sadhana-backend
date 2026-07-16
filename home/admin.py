from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HeroSlide, Statistic, WhyChooseUs, CallToAction,Testimonial


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "badge", "display_order", "is_active")
    list_filter = ("is_active",)
    list_editable = ("display_order", "is_active")
    search_fields = ("title", "badge")


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "suffix", "display_order", "is_active")
    list_filter = ("is_active",)
    list_editable = ("display_order", "is_active")
    search_fields = ("label",)


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ("title", "display_order", "is_active")
    list_filter = ("is_active",)
    list_editable = ("display_order", "is_active")
    search_fields = ("title",)


@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text", "is_active")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("title",)
    
admin.site.register(Testimonial)