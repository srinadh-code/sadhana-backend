from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import (
    EventCategory,
    Event,
)

from .serializers import (
    EventCategorySerializer,
    EventSerializer,
)

class EventCategoryAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):

        categories = EventCategory.objects.filter(
            is_active=True
        )

        serializer = EventCategorySerializer(
            categories,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = EventCategorySerializer(
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
        
class EventCategoryDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):

        category = get_object_or_404(
            EventCategory,
            pk=pk
        )

        serializer = EventCategorySerializer(
            category,
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

        category = get_object_or_404(
            EventCategory,
            pk=pk
        )

        category.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
class EventAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):

        events = Event.objects.filter(
            is_active=True
        )

        category = request.GET.get("category")

        if category:
            events = events.filter(category_id=category)

        upcoming = request.GET.get("upcoming")

        if upcoming == "true":
            events = events.filter(upcoming=True)

        elif upcoming == "false":
            events = events.filter(upcoming=False)

        serializer = EventSerializer(
            events,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = EventSerializer(
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
class EventDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk):

        event = get_object_or_404(
            Event,
            pk=pk
        )

        serializer = EventSerializer(
            event,
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

        event = get_object_or_404(
            Event,
            pk=pk
        )

        event.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )