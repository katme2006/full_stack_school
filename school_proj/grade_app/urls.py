from django.urls import path
from .views import All_grades, A_grade
from django.urls import include, path
urlpatterns = [
    path('',All_grades.as_view(), name='all_grades'),
    path("<int:id>/", A_grade.as_view(), name="a_grade"),
]

