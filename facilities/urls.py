from django.urls import path
from .views import (
    FacilityAPIView,
    FacilityAdminAPIView,
    FacilityDetailAPIView,
)

urlpatterns = [

    path(
        "",
        FacilityAPIView.as_view(),
        name="facility-list"
    ),

    path(
        "admin/",
        FacilityAdminAPIView.as_view(),
        name="facility-admin"
    ),

    path(
        "admin/<int:pk>/",
        FacilityDetailAPIView.as_view(),
        name="facility-detail"
    ),

]