from django.urls import path

from .views import (
    create_vendor,
    get_vendor_by_id,
    delete_vendor,
    get_featured_vendors,
    
)
urlpatterns = [
    # path('', get_all_products),
    path('create', create_vendor),
    path('featured', get_featured_vendors),
    path('<str:id>', get_vendor_by_id),
    path('delete/<str:id>', delete_vendor),
]