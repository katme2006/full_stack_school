from .models import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average"]

    def get_students(self, obj):
        return obj.students.count()
    
    def get_grade_average(self, obj):
        grades = obj.grades.all()
         # Check if there are no grades
        if len(grades) == 0:
            return 0  # Return a default value like 0 or None, depending on what makes sense for your application

        return round(sum([x.grade for x in grades])/len(grades),2)

