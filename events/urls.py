from django.urls import path

from .views import (
    EventCategoryAPIView,
    EventCategoryDetailAPIView,
    EventAPIView,
    EventDetailAPIView,
)

urlpatterns = [

    # ==========================================
    # EVENT CATEGORY
    # ==========================================

    path(
        "categories/",
        EventCategoryAPIView.as_view(),
        name="event-categories",
    ),

    path(
        "categories/<int:pk>/",
        EventCategoryDetailAPIView.as_view(),
        name="event-category-detail",
    ),

    # ==========================================
    # EVENTS
    # ==========================================

    path(
        "",
        EventAPIView.as_view(),
        name="events",
    ),

    path(
        "<int:pk>/",
        EventDetailAPIView.as_view(),
        name="event-detail",
    ),

]