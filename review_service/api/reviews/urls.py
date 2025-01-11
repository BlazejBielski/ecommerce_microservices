from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('review/', views.ReviewView.as_view(), name='review-list'),

]
