from django.urls import path

from .views import (
    AboutAPIView,
    AboutDetailAPIView,
    FacultyAPIView,
    FacultyDetailAPIView,
    TimelineAPIView,
    TimelineDetailAPIView,
    AchievementAPIView,
    AchievementDetailAPIView,
)

urlpatterns = [
    # About
    path("", AboutAPIView.as_view(), name="about"),
    path("<int:pk>/", AboutDetailAPIView.as_view(), name="about-detail"),

    # Faculty
    path("faculty/", FacultyAPIView.as_view(), name="faculty"),
    path("faculty/<int:pk>/", FacultyDetailAPIView.as_view(), name="faculty-detail"),

    # Timeline
    path("timeline/", TimelineAPIView.as_view(), name="timeline"),
    path("timeline/<int:pk>/", TimelineDetailAPIView.as_view(), name="timeline-detail"),

    # Achievement
    path("achievements/", AchievementAPIView.as_view(), name="achievement"),
    path(
        "achievements/<int:pk>/",
        AchievementDetailAPIView.as_view(),
        name="achievement-detail",
    ),
]