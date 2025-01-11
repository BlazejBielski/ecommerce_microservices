from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user_id', 'product_id', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user_id','created_at']



class ReviewDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'user_id',
            'product_id',
            'rating',
            'comment',
            'created_at',
            'user',
            'product_valid',
        ]
        read_only_fields = ['id', 'created_at', 'user_id']
