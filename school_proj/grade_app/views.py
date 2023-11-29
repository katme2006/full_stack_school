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
    def get_a_grade(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        return Response(GradeAllSerializer(grade).data)
    
def put(self, request, id):
        
        # Fetch the Grade object with the given id. If it doesn't exist, return a 404 response.
        grade = get_object_or_404(Grade, id=id)

        #creates an instance of the serialize
        #grade is the grade we are updating
        #request.data is a dictionary-like object that contains the parsed JSON data set that we're going to recieve from the front end ->we are putting this BACK into Python
        serializer = GradeAllSerializer(grade, data=request.data, partial = True)
        #partial = True is going to let us do partial updates, and not raise an error

        # Check if the data provided in the request is valid according to the serializer's validation rules. (the rules in any validator file or validators in your model)
        if serializer.is_valid():
            # If 'grade' field is present in the request data, we update the grade's grade field.
            if 'grade' in request.data:
                grade.grade = request.data['grade']
            # If 'a_subject' field is present in the request data, we update the grade's a_subject field.
            if 'a_subject' in request.data:
                grade.a_subject_id = request.data['a_subject']
            # If 'a_student' field is present in the request data, we update the grade's student field. (student passed in as an id)
            if 'student' in request.data:
                grade.student_id = request.data['student']

             # Save the updated grade object to the database.
            grade.save()

             # Return a successful response with the serialized grade data and a 200 OK status.
            return Response(serializer.data, status=status.HTTP_200_OK)
        

    # If the data is not valid, return a response with the error details and a 400 Bad Request status.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)