from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('musicians_delete/', views.musicians_delete)
]