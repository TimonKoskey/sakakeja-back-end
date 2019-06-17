from django.urls import path
from .views import (
    PrimarySearchResultsAPIView,
    LatestPropertyListAPIView,
    LocationListAPIView ,
    PropertyDetailsAPIView,
    
)

urlpatterns = [
    path(r'latest', LatestPropertyListAPIView.as_view()),
    path(r'search', PrimarySearchResultsAPIView.as_view()),
    path(r'locations/all', LocationListAPIView.as_view()),
    path(r'details/<int:pk>/', PropertyDetailsAPIView.as_view()),
]
