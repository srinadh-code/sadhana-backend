from django.conf import settings
from django.core.mail import send_mail
import requests
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    AdmissionHero,
    Eligibility,
    RequiredDocument,
    AdmissionEnquiry,
    FAQ,
)

from .serializers import (
    AdmissionHeroSerializer,
    EligibilitySerializer,
    RequiredDocumentSerializer,
    AdmissionEnquirySerializer,
    FAQSerializer,
)


class AdmissionAPIView(APIView):

    # permission_classes = [AllowAny]
    permission_classes= [AllowAny]


    def get(self, request):

        hero = AdmissionHero.objects.filter(
            is_active=True
        ).first()

        hero_data = None

        if hero:
            hero_data = AdmissionHeroSerializer(
                hero,
                context={"request": request}
            ).data

        eligibility = EligibilitySerializer(
            Eligibility.objects.filter(
                is_active=True
            ),
            many=True
        ).data

        documents = RequiredDocumentSerializer(
            RequiredDocument.objects.filter(
                is_active=True
            ),
            many=True
        ).data

        faqs = FAQSerializer(
            FAQ.objects.filter(
                is_active=True
            ),
            many=True
        ).data

        return Response({

            "hero": hero_data,

            "eligibility": eligibility,

            "documents": documents,

            "faqs": faqs

        })




class AdmissionEnquiryAPIView(APIView):

    # permission_classes = [AllowAny]
    permission_classes= [AllowAny]


    def post(self, request):

        serializer = AdmissionEnquirySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        enquiry = serializer.save()

        url = "https://api.brevo.com/v3/smtp/email"

        headers = {
            "accept": "application/json",
            "api-key": settings.BREVO_API_KEY,
            "content-type": "application/json",
        }

        # ----------------------------
        # Email to School
        # ----------------------------

        school_payload = {
            "sender": {
                "name": "Sadhana High School",
                "email": settings.DEFAULT_FROM_EMAIL,
            },
            "to": [
                {
                    "email": settings.DEFAULT_FROM_EMAIL,
                    "name": "Admissions Team",
                }
            ],
            "subject": "New Admission Enquiry",
            "htmlContent": f"""
            <html>
            <body>

                <h2>New Admission Enquiry</h2>

                <table border="1" cellpadding="8" cellspacing="0">

                    <tr>
                        <td><strong>Student Name</strong></td>
                        <td>{enquiry.student_name}</td>
                    </tr>

                    <tr>
                        <td><strong>Parent Name</strong></td>
                        <td>{enquiry.parent_name}</td>
                    </tr>

                    <tr>
                        <td><strong>Email</strong></td>
                        <td>{enquiry.email}</td>
                    </tr>

                    <tr>
                        <td><strong>Phone</strong></td>
                        <td>{enquiry.phone}</td>
                    </tr>

                    <tr>
                        <td><strong>Grade</strong></td>
                        <td>{enquiry.grade}</td>
                    </tr>

                    <tr>
                        <td><strong>Message</strong></td>
                        <td>{enquiry.message}</td>
                    </tr>

                </table>

            </body>
            </html>
            """,
        }

        school_response = requests.post(
            url,
            json=school_payload,
            headers=headers,
        )

        if school_response.status_code not in [200, 201]:
            return Response(
                {
                    "message": "Failed to send email to school.",
                    "error": school_response.json(),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ----------------------------
        # Email to Parent
        # ----------------------------

        parent_payload = {
            "sender": {
                "name": "Sadhana High School",
                "email": settings.DEFAULT_FROM_EMAIL,
            },
            "to": [
                {
                    "email": enquiry.email,
                    "name": enquiry.parent_name,
                }
            ],
            "subject": "Admission Enquiry Received",
            "htmlContent": f"""
            <html>
            <body>

                <h2>Admission Enquiry Received</h2>

                <p>Dear <strong>{enquiry.parent_name}</strong>,</p>

                <p>
                    Thank you for submitting an admission enquiry for
                    <strong>{enquiry.student_name}</strong>.
                </p>

                <p>
                    We have successfully received your enquiry.
                    Our admissions team will contact you shortly.
                </p>

                <br>

                <p>
                    Regards,<br>
                    <strong>Sadhana High School</strong>
                </p>

            </body>
            </html>
            """,
        }

        parent_response = requests.post(
            url,
            json=parent_payload,
            headers=headers,
        )

        if parent_response.status_code not in [200, 201]:
            return Response(
                {
                    "message": "Enquiry saved, but failed to send confirmation email.",
                    "error": parent_response.json(),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "Admission enquiry submitted successfully.",
            },
            status=status.HTTP_201_CREATED,
        )


class AdmissionEnquiryAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get(self, request):

        enquiries = AdmissionEnquiry.objects.all()

        serializer = AdmissionEnquirySerializer(
            enquiries,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": enquiries.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    

class AdmissionEnquiryDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def put(self, request, pk):

        try:
            enquiry = AdmissionEnquiry.objects.get(pk=pk)

        except AdmissionEnquiry.DoesNotExist:

            return Response(

                {

                    "message": "Enquiry not found."

                },

                status=404

            )

        serializer = AdmissionEnquirySerializer(

            enquiry,

            data=request.data,

            partial=True

        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)
    
    def delete(self, request, pk):

        try:

            enquiry = AdmissionEnquiry.objects.get(pk=pk)

        except AdmissionEnquiry.DoesNotExist:

            return Response(

                {

                    "message": "Enquiry not found."

                },

                status=404

            )

        enquiry.delete()

        return Response(

            {

                "message": "Enquiry deleted successfully."

            },

            status=204

        )
    


class AdmissionHeroAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get(self, request):

        heroes = AdmissionHero.objects.all()

        serializer = AdmissionHeroSerializer(
            heroes,
            many=True,
            context={"request": request},
        )

        return Response(
            {
                "success": True,
                "count": heroes.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        serializer = AdmissionHeroSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Admission Hero created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class AdmissionHeroDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get_object(self, pk):

        try:
            return AdmissionHero.objects.get(pk=pk)

        except AdmissionHero.DoesNotExist:
            return None

    def put(self, request, pk):

        hero = self.get_object(pk)

        if hero is None:
            return Response(
                {
                    "message": "Admission Hero not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AdmissionHeroSerializer(
            hero,
            data=request.data,
            partial=True,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Admission Hero updated successfully.",
                "data": serializer.data,
            }
        )

    def delete(self, request, pk):

        hero = self.get_object(pk)

        if hero is None:
            return Response(
                {
                    "message": "Admission Hero not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        hero.delete()

        return Response(
            {
                "success": True,
                "message": "Admission Hero deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )
    

class EligibilityAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get(self, request):

        eligibility = Eligibility.objects.all()

        serializer = EligibilitySerializer(
            eligibility,
            many=True
        )

        return Response(
            {
                "success": True,
                "count": eligibility.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        print(request.data)

        serializer = EligibilitySerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Eligibility created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    


class EligibilityDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get_object(self, pk):

        try:
            return Eligibility.objects.get(pk=pk)

        except Eligibility.DoesNotExist:
            return None

    def get(self, request, pk):

        eligibility = self.get_object(pk)

        if eligibility is None:
            return Response(
                {
                    "message": "Eligibility not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = EligibilitySerializer(eligibility)

        return Response(serializer.data)

    def put(self, request, pk):

        eligibility = self.get_object(pk)

        if eligibility is None:
            return Response(
                {
                    "message": "Eligibility not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = EligibilitySerializer(
            eligibility,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Eligibility updated successfully.",
                "data": serializer.data,
            }
        )

    def delete(self, request, pk):

        eligibility = self.get_object(pk)

        if eligibility is None:
            return Response(
                {
                    "message": "Eligibility not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        eligibility.delete()

        return Response(
            {
                "success": True,
                "message": "Eligibility deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )
    


class RequiredDocumentAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get(self, request):

        documents = RequiredDocument.objects.all()

        serializer = RequiredDocumentSerializer(
            documents,
            many=True
        )

        return Response(
            {
                "success": True,
                "count": documents.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        serializer = RequiredDocumentSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Required document created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class RequiredDocumentDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get_object(self, pk):

        try:
            return RequiredDocument.objects.get(pk=pk)

        except RequiredDocument.DoesNotExist:
            return None

    def get(self, request, pk):

        document = self.get_object(pk)

        if document is None:
            return Response(
                {
                    "message": "Required document not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RequiredDocumentSerializer(document)

        return Response(serializer.data)

    def put(self, request, pk):

        document = self.get_object(pk)

        if document is None:
            return Response(
                {
                    "message": "Required document not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RequiredDocumentSerializer(
            document,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Required document updated successfully.",
                "data": serializer.data,
            }
        )

    def delete(self, request, pk):

        document = self.get_object(pk)

        if document is None:
            return Response(
                {
                    "message": "Required document not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        document.delete()

        return Response(
            {
                "success": True,
                "message": "Required document deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )
    



class FAQAdminAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]


    def get(self, request):

        faqs = FAQ.objects.all()

        serializer = FAQSerializer(
            faqs,
            many=True
        )

        return Response(
            {
                "success": True,
                "count": faqs.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        serializer = FAQSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "FAQ created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    


class FAQDetailAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes= [AllowAny]

    def get_object(self, pk):

        try:
            return FAQ.objects.get(pk=pk)

        except FAQ.DoesNotExist:
            return None

    def get(self, request, pk):

        faq = self.get_object(pk)

        if faq is None:
            return Response(
                {
                    "message": "FAQ not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = FAQSerializer(faq)

        return Response(serializer.data)

    def put(self, request, pk):

        faq = self.get_object(pk)

        if faq is None:
            return Response(
                {
                    "message": "FAQ not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = FAQSerializer(
            faq,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "FAQ updated successfully.",
                "data": serializer.data,
            }
        )

    def delete(self, request, pk):

        faq = self.get_object(pk)

        if faq is None:
            return Response(
                {
                    "message": "FAQ not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        faq.delete()

        return Response(
            {
                "success": True,
                "message": "FAQ deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )
    



class AdmissionEnquiryReplyAPIView(APIView):

    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]

    def post(self, request, pk):

        try:
            enquiry = AdmissionEnquiry.objects.get(id=pk)

        except AdmissionEnquiry.DoesNotExist:

            return Response(
                {
                    "message": "Admission enquiry not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        reply = request.data.get("reply")

        if not reply:

            return Response(
                {
                    "message": "Reply is required."
                },
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
                "email": settings.DEFAULT_FROM_EMAIL,
            },

            "to": [
                {
                    "email": enquiry.email,
                    "name": enquiry.parent_name,
                }
            ],

            "subject": "Admission Enquiry Reply",

            "htmlContent": f"""
            <html>
            <body>

                <h2>Sadhana High School</h2>

                <p>Dear {enquiry.parent_name},</p>

                <p>{reply}</p>

                <br>

                <p>Regards,</p>

                <p>Sadhana High School</p>

            </body>
            </html>
            """,

        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
        )

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
                "message": "Reply sent successfully."
            },
            status=status.HTTP_200_OK,
        )