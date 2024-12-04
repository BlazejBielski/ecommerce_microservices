from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import CustomUserView

app_name = "users"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", CustomUserView.as_view(), name="user-list-create"),
    path('users/<uuid:pk>/', CustomUserView.as_view(), name='get_user'),
]
