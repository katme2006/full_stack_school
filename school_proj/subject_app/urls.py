from django.urls import path
from .views import All_subjects, A_subject
from django.urls import include, path

urlpatterns = [
    path('',All_subjects.as_view(), name='all_subjects'),
    path("<str:subject_name>/", A_subject.as_view(), name="a_subject"),
]
