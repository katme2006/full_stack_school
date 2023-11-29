from rest_framework import serializers
from .models import Grade
from subject_app.serializers import SubjectSerializer
from student_app.serializers import StudentSerializer


class GradeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

