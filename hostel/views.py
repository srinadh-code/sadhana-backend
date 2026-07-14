from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import (
    HostelInfo,
    HostelRoom,
)

from .serializers import (
    HostelInfoSerializer,
    HostelRoomSerializer,
)


# =====================================================
# HOSTEL INFORMATION
# =====================================================
class HostelInfoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        hostel = HostelInfo.objects.first()

        if hostel:
            serializer = HostelInfoSerializer(
                hostel,
                context={"request": request},
            )
            return Response(serializer.data)

        return Response({
            "title": "",
            "subtitle": "",
            "description": "",
            "image": None
        })


# =====================================================
# HOSTEL INFORMATION ADMIN
# =====================================================

class HostelInfoAdminAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get(self, request):

        hostel = HostelInfo.objects.first()

        if not hostel:
            return Response(
                {"message": "Hostel information not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = HostelInfoSerializer(
            hostel,
            context={"request": request}
        )

        return Response(serializer.data)

    def put(self, request):
        print(request.data)
        print(request.FILES)

        hostel = HostelInfo.objects.first()

        if not hostel:

            serializer = HostelInfoSerializer(
                data=request.data,
                context={"request": request},
            )

        else:

            serializer = HostelInfoSerializer(
                hostel,
                data=request.data,
                partial=True,
                context={"request": request},
            )

        if serializer.is_valid():

            serializer.save()

            return Response(
                HostelInfoSerializer(
                    serializer.instance,
                    context={"request": request},
                ).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# =====================================================
# HOSTEL ROOMS (PUBLIC)
# =====================================================

class HostelRoomAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        rooms = HostelRoom.objects.filter(
            is_active=True
        )

        serializer = HostelRoomSerializer(
            rooms,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


# =====================================================
# HOSTEL ROOMS ADMIN
# =====================================================

class HostelRoomAdminAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get(self, request):

        rooms = HostelRoom.objects.all()

        serializer = HostelRoomSerializer(
            rooms,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    def post(self, request):

        print(request.FILES)
        print(request.data)

        serializer = HostelRoomSerializer(
            data=request.data,
            context={"request": request},
        )

        if serializer.is_valid():

            room= serializer.save()
            print(room.image)

            return Response(
                HostelRoomSerializer(
                    serializer.instance,
                    context={"request": request},
                ).data,
                status=status.HTTP_201_CREATED,
            )
        print(serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# =====================================================
# ROOM DETAIL
# =====================================================

class HostelRoomDetailAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get_object(self, pk):

        return get_object_or_404(
            HostelRoom,
            pk=pk,
        )

    def get(self, request, pk):

        serializer = HostelRoomSerializer(
            self.get_object(pk),
            context={"request": request},
        )

        return Response(serializer.data)

    def put(self, request, pk):

        room = self.get_object(pk)

        serializer = HostelRoomSerializer(
            room,
            data=request.data,
            partial=True,
            context={"request": request},
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                HostelRoomSerializer(
                    serializer.instance,
                    context={"request": request},
                ).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):

        room = self.get_object(pk)

        room.delete()

        return Response(
            {
                "message": "Room deleted successfully"
            },
            status=status.HTTP_200_OK,
        )
    




# =====================================================
# HOSTEL FACILITIES (PUBLIC)
# =====================================================

from .models import HostelFacility
from .serializers import HostelFacilitySerializer


class HostelFacilityAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        facilities = HostelFacility.objects.filter(
            is_active=True
        )

        serializer = HostelFacilitySerializer(
            facilities,
            many=True
        )

        return Response(serializer.data)


# =====================================================
# HOSTEL FACILITIES ADMIN
# =====================================================

class HostelFacilityAdminAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get(self, request):

        facilities = HostelFacility.objects.all()

        serializer = HostelFacilitySerializer(
            facilities,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = HostelFacilitySerializer(
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


# =====================================================
# HOSTEL FACILITY DETAIL
# =====================================================

class HostelFacilityDetailAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get_object(self, pk):

        return get_object_or_404(
            HostelFacility,
            pk=pk
        )

    def get(self, request, pk):

        serializer = HostelFacilitySerializer(
            self.get_object(pk)
        )

        return Response(serializer.data)

    def put(self, request, pk):

        facility = self.get_object(pk)

        serializer = HostelFacilitySerializer(
            facility,
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

        facility = self.get_object(pk)

        facility.delete()

        return Response(
            {
                "message": "Facility deleted successfully"
            },
            status=status.HTTP_200_OK
        )



# =====================================================
# HOSTEL RULES (PUBLIC)
# =====================================================

from .models import HostelRule
from .serializers import HostelRuleSerializer


class HostelRuleAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        rules = HostelRule.objects.filter(
            is_active=True
        )

        serializer = HostelRuleSerializer(
            rules,
            many=True
        )

        return Response(serializer.data)


# =====================================================
# HOSTEL RULES ADMIN
# =====================================================

class HostelRuleAdminAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get(self, request):

        rules = HostelRule.objects.all()

        serializer = HostelRuleSerializer(
            rules,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = HostelRuleSerializer(
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


# =====================================================
# HOSTEL RULE DETAIL
# =====================================================

class HostelRuleDetailAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get_object(self, pk):

        return get_object_or_404(
            HostelRule,
            pk=pk
        )

    def get(self, request, pk):

        serializer = HostelRuleSerializer(
            self.get_object(pk)
        )

        return Response(serializer.data)

    def put(self, request, pk):

        rule = self.get_object(pk)

        serializer = HostelRuleSerializer(
            rule,
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

        rule = self.get_object(pk)

        rule.delete()

        return Response(
            {
                "message": "Rule deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    




# =====================================================
# HOSTEL ENQUIRY (PUBLIC)
# =====================================================

from .models import HostelEnquiry
from .serializers import HostelEnquirySerializer


class HostelEnquiryAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = HostelEnquirySerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Enquiry submitted successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# =====================================================
# HOSTEL ENQUIRIES ADMIN
# =====================================================

class HostelEnquiryAdminAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get(self, request):

        enquiries = HostelEnquiry.objects.all()

        serializer = HostelEnquirySerializer(
            enquiries,
            many=True,
        )

        return Response(serializer.data)


# =====================================================
# HOSTEL ENQUIRY DETAIL
# =====================================================

class HostelEnquiryDetailAPIView(APIView):

    # Later change to IsAdminUser
    permission_classes = [AllowAny]

    def get_object(self, pk):

        return get_object_or_404(
            HostelEnquiry,
            pk=pk,
        )

    def get(self, request, pk):

        serializer = HostelEnquirySerializer(
            self.get_object(pk)
        )

        return Response(serializer.data)

    def delete(self, request, pk):

        enquiry = self.get_object(pk)

        enquiry.delete()

        return Response(
            {
                "message": "Enquiry deleted successfully"
            },
            status=status.HTTP_200_OK,
        )