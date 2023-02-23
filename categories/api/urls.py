from rest_framework.urls import path

from .views import (
    get_root_categories,
    get_featured_categories,
    get_all_categories
)

urlpatterns = [
    path('', get_all_categories),
    path('roots', get_root_categories),
    path('featured', get_featured_categories),
]
