from django.urls import path

from .views import (
    AdmissionAPIView,
    AdmissionEnquiryAPIView,
    AdmissionEnquiryAdminAPIView,
    AdmissionEnquiryDetailAPIView,
    AdmissionHeroAdminAPIView,
    AdmissionHeroDetailAPIView,
    EligibilityAdminAPIView,
    EligibilityDetailAPIView,
    RequiredDocumentAdminAPIView,
    RequiredDocumentDetailAPIView ,
    FAQAdminAPIView,
    FAQDetailAPIView,
    AdmissionEnquiryReplyAPIView,
)

urlpatterns = [

    # Public APIs
    path(
        "",
        AdmissionAPIView.as_view(),
        name="admission-page",
    ),

    path(
        "enquiry/",
        AdmissionEnquiryAPIView.as_view(),
        name="admission-enquiry",
    ),

    # Admin Enquiry APIs
    path(
        "admin/enquiries/",
        AdmissionEnquiryAdminAPIView.as_view(),
        name="admin-enquiries",
    ),

    path(
        "admin/enquiries/<int:pk>/",
        AdmissionEnquiryDetailAPIView.as_view(),
        name="admin-enquiry-detail",
    ),
    path(
    "admin/hero/",
    AdmissionHeroAdminAPIView.as_view(),
    name="admin-hero",
),

path(
    "admin/hero/<int:pk>/",
    AdmissionHeroDetailAPIView.as_view(),
    name="admin-hero-detail",
),

path(
    "admin/eligibility/",
    EligibilityAdminAPIView.as_view(),
    name="admin-eligibility",
),

path(
    "admin/eligibility/<int:pk>/",
    EligibilityDetailAPIView.as_view(),
    name="admin-eligibility-detail",
),

path(
    "admin/documents/",
    RequiredDocumentAdminAPIView.as_view(),
    name="admin-documents",
),

path(
    "admin/documents/<int:pk>/",
    RequiredDocumentDetailAPIView.as_view(),
    name="admin-document-detail",
),

path(
    "admin/faqs/",
    FAQAdminAPIView.as_view(),
    name="admin-faqs",
),

path(
    "admin/faqs/<int:pk>/",
    FAQDetailAPIView.as_view(),
    name="admin-faq-detail",
),

path(
    "admin/enquiries/<int:pk>/reply/",
    AdmissionEnquiryReplyAPIView.as_view(),
    name="admin-admission-enquiry-reply",
),
]