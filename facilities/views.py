from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status

from .models import Facility
from .serializers import FacilitySerializer


class FacilityAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        facilities = Facility.objects.filter(is_active=True)

        serializer = FacilitySerializer(
    facilities,
    many=True,
    context={"request": request}
)

        return Response(serializer.data)


class FacilityAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes=[AllowAny]

    def get(self, request):

        facilities = Facility.objects.all()

        serializer = FacilitySerializer(
    facilities,
    many=True,
    context={"request": request}
)
        return Response(serializer.data)

    def post(self, request):


        print(request.FILES)
        print(request.data)
        serializer = FacilitySerializer(
    data=request.data,
    context={"request": request}
)

        if serializer.is_valid():

            facility=serializer.save()

            print("IMAGE AFTER SAVE:", facility.image)

            return Response(
    FacilitySerializer(
        serializer.instance,
        context={"request": request}
    ).data,
    status=status.HTTP_201_CREATED
)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FacilityDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]

    permission_classes = [AllowAny]
    def get_object(self, pk):
        return get_object_or_404(Facility, pk=pk)

    def get(self, request, pk):

        serializer = FacilitySerializer(
    self.get_object(pk),
    context={"request": request}
)

        return Response(serializer.data)

    def put(self, request, pk):

        facility = self.get_object(pk)

        serializer = FacilitySerializer(
            facility,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
    FacilitySerializer(
        serializer.instance,
        context={"request": request}
    ).data
)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        facility = self.get_object(pk)

        facility.delete()

        return Response(
            {
                "message": "Facility deleted successfully"
            },
            status=status.HTTP_200_OK
        )