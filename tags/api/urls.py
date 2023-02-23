from django.urls import path

from .views import get_all_tags

urlpatterns = [
    path('', get_all_tags)
]