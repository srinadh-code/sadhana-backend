from django.urls import path
from .views import (
    HeroSlideListCreateAPIView,
    HeroSlideDetailAPIView,
    StatisticListCreateAPIView,
    StatisticDetailAPIView,
    WhyChooseUsListCreateAPIView,
    WhyChooseUsDetailAPIView,
    CallToActionListCreateAPIView,
    CallToActionDetailAPIView,
)

urlpatterns = [
    # Hero Slides
    path(
        "hero-slides/",
        HeroSlideListCreateAPIView.as_view(),
        name="hero-slide-list-create",
    ),
    path(
        "hero-slides/<int:pk>/",
        HeroSlideDetailAPIView.as_view(),
        name="hero-slide-detail",
    ),

    # Statistics
    path(
        "statistics/",
        StatisticListCreateAPIView.as_view(),
        name="statistic-list-create",
    ),
    path(
        "statistics/<int:pk>/",
        StatisticDetailAPIView.as_view(),
        name="statistic-detail",
    ),

    # Why Choose Us
    path(
        "why-choose-us/",
        WhyChooseUsListCreateAPIView.as_view(),
        name="why-choose-us-list-create",
    ),
    path(
        "why-choose-us/<int:pk>/",
        WhyChooseUsDetailAPIView.as_view(),
        name="why-choose-us-detail",
    ),

    # Call To Action
    path(
        "call-to-action/",
        CallToActionListCreateAPIView.as_view(),
        name="cta-list-create",
    ),
    path(
        "call-to-action/<int:pk>/",
        CallToActionDetailAPIView.as_view(),
        name="cta-detail",
    ),
]