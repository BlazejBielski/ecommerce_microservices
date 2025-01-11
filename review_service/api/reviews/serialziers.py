from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user_id', 'product_id', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user_id','created_at']
