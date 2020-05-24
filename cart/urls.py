from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('add/<photo_id>', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('remove/<photo_id>', remove_from_cart, name='remove_from_cart')
    ]
