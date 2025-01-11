from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Review

import requests

from .serialziers import ReviewSerializer
from .utils import get_user_details, verify_product


class ReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.user_id

        product_id = data.get('product_id')
        if not product_id or not verify_product(product_id):
            return Response({'error': 'Invalid or non-existent product_id'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        for review in response.data:
            # Pobierz szczegóły użytkownika
            user_details = get_user_details(review['user_id'])
            review['user'] = user_details if "error" not in user_details else None

            # Opcjonalna weryfikacja produktu (jeśli potrzebna)
            if not verify_product(review['product_id']):
                review['product_valid'] = False
            else:
                review['product_valid'] = True

        return response


class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        review = self.get_object()

        # Pobierz szczegóły użytkownika
        user_details = get_user_details(review.user_id)
        if "error" not in user_details:
            response.data['user'] = user_details
        else:
            response.data['user'] = {'error': 'User details unavailable'}

        return response
