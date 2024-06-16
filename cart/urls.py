from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    path('add/<int:movie_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:movie_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
]
