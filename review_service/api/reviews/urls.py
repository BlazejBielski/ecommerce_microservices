from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.ReviewCreateView.as_view(), name='create_review'),
    path('reviews/<int:product_id>/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:review_id>/', views.ReviewDetailView.as_view(), name='review_details'),

]
