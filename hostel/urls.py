from django.urls import path

from .views import (
    HostelInfoAPIView,
    HostelInfoAdminAPIView,

    HostelRoomAPIView,
    HostelRoomAdminAPIView,
    HostelRoomDetailAPIView,

    HostelFacilityAPIView,
    HostelFacilityAdminAPIView,
    HostelFacilityDetailAPIView,

    HostelRuleAPIView,
    HostelRuleAdminAPIView,
    HostelRuleDetailAPIView,

    HostelEnquiryAPIView,
    HostelEnquiryAdminAPIView,
    HostelEnquiryDetailAPIView,
)

urlpatterns = [

    # =====================================================
    # PUBLIC APIs
    # =====================================================

    path(
        "info/",
        HostelInfoAPIView.as_view(),
        name="hostel-info",
    ),

    path(
        "rooms/",
        HostelRoomAPIView.as_view(),
        name="hostel-rooms",
    ),

    path(
        "facilities/",
        HostelFacilityAPIView.as_view(),
        name="hostel-facilities",
    ),

    path(
        "rules/",
        HostelRuleAPIView.as_view(),
        name="hostel-rules",
    ),

    path(
        "enquiry/",
        HostelEnquiryAPIView.as_view(),
        name="hostel-enquiry",
    ),

    # =====================================================
    # ADMIN APIs
    # =====================================================

    # Hostel Info
    path(
        "admin/info/",
        HostelInfoAdminAPIView.as_view(),
        name="admin-hostel-info",
    ),

    # Rooms
    path(
        "admin/rooms/",
        HostelRoomAdminAPIView.as_view(),
        name="admin-hostel-rooms",
    ),

    path(
        "admin/rooms/<int:pk>/",
        HostelRoomDetailAPIView.as_view(),
        name="admin-hostel-room-detail",
    ),

    # Facilities
    path(
        "admin/facilities/",
        HostelFacilityAdminAPIView.as_view(),
        name="admin-hostel-facilities",
    ),

    path(
        "admin/facilities/<int:pk>/",
        HostelFacilityDetailAPIView.as_view(),
        name="admin-hostel-facility-detail",
    ),

    # Rules
    path(
        "admin/rules/",
        HostelRuleAdminAPIView.as_view(),
        name="admin-hostel-rules",
    ),

    path(
        "admin/rules/<int:pk>/",
        HostelRuleDetailAPIView.as_view(),
        name="admin-hostel-rule-detail",
    ),

    # Enquiries
    path(
        "admin/enquiries/",
        HostelEnquiryAdminAPIView.as_view(),
        name="admin-hostel-enquiries",
    ),

    path(
        "admin/enquiries/<int:pk>/",
        HostelEnquiryDetailAPIView.as_view(),
        name="admin-hostel-enquiry-detail",
    ),
]