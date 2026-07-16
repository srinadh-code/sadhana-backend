from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import HeroSlide, Statistic, WhyChooseUs, CallToAction
from .serializers import (
    HeroSlideSerializer,
    StatisticSerializer,
    WhyChooseUsSerializer,
    CallToActionSerializer,
)


# ---------------- Hero Slides ----------------

class HeroSlideListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        slides = HeroSlide.objects.filter(is_active=True).order_by("display_order")
        serializer = HeroSlideSerializer(slides, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSlideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroSlideDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return HeroSlide.objects.get(pk=pk)

    def put(self, request, pk):
        slide = self.get_object(pk)
        serializer = HeroSlideSerializer(slide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        slide = self.get_object(pk)
        slide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------- Statistics ----------------

class StatisticListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        stats = Statistic.objects.filter(is_active=True).order_by("display_order")
        serializer = StatisticSerializer(stats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatisticDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Statistic.objects.get(pk=pk)

    def put(self, request, pk):
        stat = self.get_object(pk)
        serializer = StatisticSerializer(stat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stat = self.get_object(pk)
        stat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------- Why Choose Us ----------------

class WhyChooseUsListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        items = WhyChooseUs.objects.filter(is_active=True).order_by("display_order")
        serializer = WhyChooseUsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WhyChooseUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyChooseUsDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return WhyChooseUs.objects.get(pk=pk)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = WhyChooseUsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------- Call To Action ----------------

class CallToActionListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        cta = CallToAction.objects.filter(is_active=True)
        serializer = CallToActionSerializer(cta, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CallToActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallToActionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return CallToAction.objects.get(pk=pk)

    def put(self, request, pk):
        cta = self.get_object(pk)
        serializer = CallToActionSerializer(cta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cta = self.get_object(pk)
        cta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)