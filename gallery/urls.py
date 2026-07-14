from django.urls import path
from .views import (
    GalleryListCreateAPIView,
    GalleryDetailAPIView,
)

urlpatterns = [

    path(
        "",
        GalleryListCreateAPIView.as_view(),
        name="gallery-list-create",
    ),

    path(
        "<int:pk>/",
        GalleryDetailAPIView.as_view(),
        name="gallery-detail",
    ),

]