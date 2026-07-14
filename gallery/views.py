from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Gallery
from .serializers import GallerySerializer
from .permissions import IsSuperAdmin


class GalleryListCreateAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSuperAdmin()]

    def get(self, request):
        queryset = Gallery.objects.filter(is_active=True)

        category = request.GET.get("category")

        if category:
            queryset = queryset.filter(category=category)

        queryset = queryset.order_by("display_order", "-created_at")

        serializer = GallerySerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = GallerySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Gallery image uploaded successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
import cloudinary.uploader
from django.shortcuts import get_object_or_404


class GalleryDetailAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSuperAdmin()]

    def get(self, request, pk):
        gallery = get_object_or_404(
            Gallery,
            pk=pk,
            is_active=True
        )

        serializer = GallerySerializer(gallery)

        return Response(serializer.data)

    def put(self, request, pk):

        gallery = get_object_or_404(Gallery, pk=pk)

        

        serializer = GallerySerializer(
            gallery,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            # Delete old Cloudinary image if replaced
            return Response(
                {
                    "message": "Gallery updated successfully.",
                    "data": serializer.data,
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):

        gallery = get_object_or_404(Gallery, pk=pk)

        if gallery.image:
            try:
                cloudinary.uploader.destroy(
                    gallery.image.public_id
                )
            except Exception:
                pass

        gallery.delete()

        return Response(
            {
                "message": "Gallery deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )