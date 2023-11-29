from django.shortcuts import render
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
    
class A_subject(APIView):
    def get(self, request, subject_name):
        try:
            # Attempt to get the subject; adjust field name as necessary
            subject = Subject.objects.get(subject_name__iexact=subject_name)
            return Response(SubjectSerializer(subject).data)
        except Subject.DoesNotExist:
            # If the subject is not found, return a 'Not Found' response
            return Response({"error": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)