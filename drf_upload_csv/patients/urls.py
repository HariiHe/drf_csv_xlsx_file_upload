"""Contains all urls for patients app."""
from django.urls import re_path
from patients import views

urlpatterns = [
    re_path(r'^csv_upload/$', views.FileUploadView.as_view()),
    re_path(r'^list/$', views.PatientListAPIView.as_view())
]
