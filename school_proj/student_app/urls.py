from django.urls import path
from .views import All_students,A_Student

urlpatterns = [
    path("", All_students.as_view(), name='all_students'),
    path("<int:id>/",A_Student.as_view(),name ="a_student" )
]
