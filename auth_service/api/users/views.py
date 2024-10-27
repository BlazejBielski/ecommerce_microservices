from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import CustomUserSerializer


class CustomUserView(APIView):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(self.queryset, pk=pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            users = self.queryset.all()
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method 'PUT' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method 'DELETE' not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
