from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import (
    AcademicHero,
    AcademicProgram,
    TeachingMethod,
    Department,
    AcademicCalendar,
    AcademicDownload,
)

from .serializers import (
    AcademicHeroSerializer,
    AcademicProgramSerializer,
    TeachingMethodSerializer,
    DepartmentSerializer,
    AcademicCalendarSerializer,
    AcademicDownloadSerializer,
)
class AcademicHeroAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        hero = AcademicHero.objects.filter(is_active=True).first()

        if not hero:
            return Response({})

        serializer = AcademicHeroSerializer(hero)
        return Response(serializer.data)

    def post(self, request):
        serializer = AcademicHeroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AcademicHeroDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        hero = get_object_or_404(AcademicHero, pk=pk)

        serializer = AcademicHeroSerializer(
            hero,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hero = get_object_or_404(AcademicHero, pk=pk)
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AcademicProgramAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        programs = AcademicProgram.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = AcademicProgramSerializer(
            programs,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AcademicProgramSerializer(
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
        
class AcademicProgramDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        program = get_object_or_404(
            AcademicProgram,
            pk=pk
        )

        serializer = AcademicProgramSerializer(
            program,
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
        program = get_object_or_404(
            AcademicProgram,
            pk=pk
        )

        program.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class TeachingMethodAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        methods = TeachingMethod.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = TeachingMethodSerializer(
            methods,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = TeachingMethodSerializer(
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


class TeachingMethodDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        method = get_object_or_404(
            TeachingMethod,
            pk=pk
        )

        serializer = TeachingMethodSerializer(
            method,
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
        method = get_object_or_404(
            TeachingMethod,
            pk=pk
        )

        method.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class DepartmentAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        departments = Department.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = DepartmentSerializer(
            departments,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(
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


class DepartmentDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        department = get_object_or_404(
            Department,
            pk=pk
        )

        serializer = DepartmentSerializer(
            department,
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
        department = get_object_or_404(
            Department,
            pk=pk
        )

        department.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class AcademicCalendarAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        calendar = AcademicCalendar.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = AcademicCalendarSerializer(
            calendar,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AcademicCalendarSerializer(
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


class AcademicCalendarDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        calendar = get_object_or_404(
            AcademicCalendar,
            pk=pk
        )

        serializer = AcademicCalendarSerializer(
            calendar,
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
        calendar = get_object_or_404(
            AcademicCalendar,
            pk=pk
        )

        calendar.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class AcademicDownloadAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        downloads = AcademicDownload.objects.filter(
            is_active=True
        ).order_by("display_order")

        serializer = AcademicDownloadSerializer(
            downloads,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AcademicDownloadSerializer(
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


class AcademicDownloadDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        download = get_object_or_404(
            AcademicDownload,
            pk=pk
        )

        serializer = AcademicDownloadSerializer(
            download,
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
        download = get_object_or_404(
            AcademicDownload,
            pk=pk
        )

        download.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )