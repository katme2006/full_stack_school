from django.shortcuts import render
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Grade
from .serializers import GradeAllSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class All_grades(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serialized_grades = GradeAllSerializer(grades, many=True)
        return Response(serialized_grades.data)
    
class A_grade(APIView):
    def get(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        return Response(GradeAllSerializer(grade).data)
    
    # def put(self,request,id):
    #     grade = Grade.objects.get(id = id)
