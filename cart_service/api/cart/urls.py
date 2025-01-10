from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/', views.AddItemView.as_view(), name='add-item-to-cart'),
]
