from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .models import ContactInfo, ContactEnquiry
from .serializers import (
    ContactInfoSerializer,
    ContactEnquirySerializer,
)
from rest_framework.permissions import AllowAny

class ContactInfoAPIView(APIView):

    def get(self, request):

        contact = ContactInfo.objects.first()

        if not contact:
            return Response(
                {"message": "Contact information not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ContactInfoSerializer(contact)

        return Response(serializer.data)


class ContactEnquiryAPIView(APIView):

    def post(self, request):

        serializer = ContactEnquirySerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Thank you! Your enquiry has been submitted successfully."
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    



from rest_framework.permissions import IsAdminUser


class ContactInfoAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]

    def get(self, request):

        contact = ContactInfo.objects.first()

        serializer = ContactInfoSerializer(contact)

        return Response(serializer.data)

    def put(self, request):

        contact = ContactInfo.objects.first()

        serializer = ContactInfoSerializer(
            contact,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Contact information updated successfully."
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ContactEnquiryAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]

    def get(self, request):

        enquiries = ContactEnquiry.objects.all()

        serializer = ContactEnquirySerializer(
            enquiries,
            many=True
        )

        return Response(serializer.data)
    

class ContactEnquiryStatusAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]

    def patch(self, request, pk):

        try:
            enquiry = ContactEnquiry.objects.get(id=pk)

        except ContactEnquiry.DoesNotExist:
            return Response(
                {"message": "Enquiry not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        enquiry.status = request.data.get(
            "status",
            enquiry.status
        )

        enquiry.save()

        return Response(
            {
                "message": "Status updated successfully."
            }
        )
    



class ContactEnquiryReplyAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]

    def post(self, request, pk):

        try:
            enquiry = ContactEnquiry.objects.get(id=pk)

        except ContactEnquiry.DoesNotExist:
            return Response(
                {"message": "Enquiry not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        reply = request.data.get("reply")

        if not reply:
            return Response(
                {"message": "Reply is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        url = "https://api.brevo.com/v3/smtp/email"

        headers = {
            "accept": "application/json",
            "api-key": settings.BREVO_API_KEY,
            "content-type": "application/json",
        }

        payload = {
            "sender": {
                "name": "Sadhana High School",
                "email": settings.DEFAULT_FROM_EMAIL,   # Verified sender email
            },
            "to": [
                {
                    "email": enquiry.email,
                    "name": enquiry.full_name,
                }
            ],
            "subject": f"Re: {enquiry.subject}",
            "htmlContent": f"""
                <html>
                <body>

                    <h2>Sadhana High School</h2>

                    <p>Dear {enquiry.full_name},</p>

                    <p>{reply}</p>

                    <br>

                    <p>Thank you for contacting us.</p>

                    <p>Regards,<br>
                    Sadhana High School</p>

                </body>
                </html>
            """,
        }
        print(settings.DEFAULT_FROM_EMAIL)
        response = requests.post(
            url,
            json=payload,
            headers=headers,
        )
        print(response.status_code)
        print(response.text)
        print(settings.BREVO_API_KEY)
        if response.status_code not in [200, 201]:
            return Response(
                {
                    "message": "Failed to send email.",
                    "error": response.json(),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        enquiry.status = "replied"
        enquiry.save()

        return Response(
            {
                "success": True,
                "message": "Reply sent successfully.",
            },
            status=status.HTTP_200_OK,
        )