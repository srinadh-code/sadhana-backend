from django.urls import path

from .views import (
    AcademicHeroAPIView,
    AcademicHeroDetailAPIView,
    AcademicProgramAPIView,
    AcademicProgramDetailAPIView,
    TeachingMethodAPIView,
    TeachingMethodDetailAPIView,
    DepartmentAPIView,
    DepartmentDetailAPIView,
    AcademicCalendarAPIView,
    AcademicCalendarDetailAPIView,
    AcademicDownloadAPIView,
    AcademicDownloadDetailAPIView,
)

urlpatterns = [

    # Hero
    path(
        "hero/",
        AcademicHeroAPIView.as_view(),
        name="academic-hero",
    ),
    path(
        "hero/<int:pk>/",
        AcademicHeroDetailAPIView.as_view(),
        name="academic-hero-detail",
    ),

    # Programs
    path(
        "programs/",
        AcademicProgramAPIView.as_view(),
        name="academic-programs",
    ),
    path(
        "programs/<int:pk>/",
        AcademicProgramDetailAPIView.as_view(),
        name="academic-program-detail",
    ),

    # Teaching Methods
    path(
        "methods/",
        TeachingMethodAPIView.as_view(),
        name="teaching-methods",
    ),
    path(
        "methods/<int:pk>/",
        TeachingMethodDetailAPIView.as_view(),
        name="teaching-method-detail",
    ),

    # Departments
    path(
        "departments/",
        DepartmentAPIView.as_view(),
        name="departments",
    ),
    path(
        "departments/<int:pk>/",
        DepartmentDetailAPIView.as_view(),
        name="department-detail",
    ),

    # Calendar
    path(
        "calendar/",
        AcademicCalendarAPIView.as_view(),
        name="academic-calendar",
    ),
    path(
        "calendar/<int:pk>/",
        AcademicCalendarDetailAPIView.as_view(),
        name="academic-calendar-detail",
    ),

    # Downloads
    path(
        "downloads/",
        AcademicDownloadAPIView.as_view(),
        name="academic-downloads",
    ),
    path(
        "downloads/<int:pk>/",
        AcademicDownloadDetailAPIView.as_view(),
        name="academic-download-detail",
    ),
]