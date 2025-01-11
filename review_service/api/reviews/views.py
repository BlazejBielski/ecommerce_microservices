from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review


class ReviewView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        reviews_data = [{
            'user_id': review.user_id,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at,
        } for review in reviews]
        return Response(reviews_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        review = Review(
            product_id=data['product_id'],
            rating=data['rating'],
            comment=data['comment'],
            user_id=data['user_id'],
        )
        return Response({'review_id': review.id,
                         'status': 'success',
                         }, status=status.HTTP_201_CREATED)
