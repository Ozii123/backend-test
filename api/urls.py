from django.urls import include, path
from rest_framework import routers
from .views import SectionView


urlpatterns = [
    path('sections/<str:pk>',SectionView.as_view()),
    path('sections/',SectionView.as_view()),
]