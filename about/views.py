from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import (
    About,
    Faculty,
    Timeline,
    Achievement,
)

from .serializers import (
    AboutSerializer,
    FacultySerializer,
    TimelineSerializer,
    AchievementSerializer,
)


class AboutAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        about = About.objects.filter(is_active=True).first()

        if not about:
            return Response({})

        serializer = AboutSerializer(about)
        return Response(serializer.data)

    def post(self, request):

        if About.objects.exists():
            return Response(
                {"error": "About page already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AboutSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
class AboutDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):

        about = get_object_or_404(
            About,
            pk=pk
        )

        serializer = AboutSerializer(
            about,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        about = get_object_or_404(
            About,
            pk=pk
        )

        about.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class FacultyAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        faculty = Faculty.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = FacultySerializer(
            faculty,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FacultyDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        faculty = get_object_or_404(
            Faculty,
            pk=pk
        )

        serializer = FacultySerializer(
            faculty,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        faculty = get_object_or_404(
            Faculty,
            pk=pk
        )

        faculty.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class TimelineAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        timeline = Timeline.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = TimelineSerializer(
            timeline,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = TimelineSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TimelineDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        timeline = get_object_or_404(
            Timeline,
            pk=pk
        )

        serializer = TimelineSerializer(
            timeline,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        timeline = get_object_or_404(
            Timeline,
            pk=pk
        )

        timeline.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
class AchievementAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        achievements = Achievement.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = AchievementSerializer(
            achievements,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AchievementSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AchievementDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        achievement = get_object_or_404(
            Achievement,
            pk=pk
        )

        serializer = AchievementSerializer(
            achievement,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        achievement = get_object_or_404(
            Achievement,
            pk=pk
        )

        achievement.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )