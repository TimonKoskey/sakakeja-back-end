from django.urls import path
from .views import (
	SignInUsers,
	SignUpUsers,
	CreateNewPropertyAPIView
)

urlpatterns = [
    path(r'auth', SignInUsers.as_view()),
	path(r'register', SignUpUsers.as_view()),
    path(r'property/upload', CreateNewPropertyAPIView.as_view()),
    ]
