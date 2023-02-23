from django.urls import path

from .views import (
    create_product,
    get_product_by_handle,
    delete_product,
    get_all_products,
    get_recommended_products,
    get_product_by_category,
    create_checkout_session,
    create_index,
    delete_duplicates,
    get_category_preview,
    get_recommended_preview
)
urlpatterns = [
    path('', get_all_products),
    path('category_preview/<str:category>' , get_category_preview),
    path('delete_duplicates', delete_duplicates),
    path('create_index', create_index),
    path('create', create_product),
    path('create-checkout-session', create_checkout_session),
    path('recommended', get_recommended_products),
    path('recommended_preview', get_recommended_preview),
    path('<str:handle>', get_product_by_handle),
    path('category/<str:category>', get_product_by_category),
    path('delete/<str:id>', delete_product),
]