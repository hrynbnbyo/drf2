from django.urls import path

from day2 import views

urlpatterns = [
    path("users/", views.UserAPIView.as_view()),
    path("users/<str:id>/", views.UserAPIView.as_view()),
    path("employee/", views.StudentAPIView.as_view()),
    path("employee/<str:id>/", views.StudentAPIView.as_view()),
]
