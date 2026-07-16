from django.urls import path

from .views import (
    ContactInfoAPIView,
    ContactEnquiryAPIView,
    ContactInfoAdminAPIView,
    ContactEnquiryAdminAPIView,
    ContactEnquiryStatusAPIView,
    ContactEnquiryReplyAPIView,
)

urlpatterns = [

    path(
        "",
        ContactInfoAPIView.as_view(),
        name="contact-info",
    ),

    path(
        "enquiry/",
        ContactEnquiryAPIView.as_view(),
        name="contact-enquiry",
    ),

    path(
        "admin/info/",
        ContactInfoAdminAPIView.as_view(),
        name="contact-admin-info",
    ),

    path(
        "admin/enquiries/",
        ContactEnquiryAdminAPIView.as_view(),
        name="contact-admin-enquiries",
    ),

    path(
        "admin/enquiries/<int:pk>/",
        ContactEnquiryStatusAPIView.as_view(),
        name="contact-status",
    ),
    path(
    "admin/enquiries/<int:pk>/reply/",
    ContactEnquiryReplyAPIView.as_view(),
    name="contact-reply",
),
]