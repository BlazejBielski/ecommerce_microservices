from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import request

from api.cart.models import Cart, CartItem


class CartView(APIView):
    def get(self,request, user_id):
        auth_response = request.get(f"http://auth_service/users/{user_id}")
        if auth_response.status_code != 200:
            return Response(auth_response.json(), status=status.HTTP_401_UNAUTHORIZED)

        cart = Cart.objects.prefetch_related("items").filter(user_id=user_id).first()
        if not cart:
            return Response({"user_id": user_id, 'items': []})

        items = []
        for item in cart.items.all():
            product_response = request.get(f"http://product_service/products/{item.product_id}")
            if product_response.status_code == 200:
                product_data = product_response.json()
                items.append({
                    'product_id': item.product_id,
                    'quantity': item.quantity,
                    'price': item.price,
                    'name': item.name,
                    'image': item.image,
                })

        return Response({"user_id": user_id, 'cart_id': cart.cart_id, 'items': items})


class AddItemView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        auth_response = request.get(f"http://auth_service/users/{user_id}")
        if auth_response.status_code != 200:
            return Response(auth_response.json(), status=status.HTTP_401_UNAUTHORIZED)

        product_response = request.get(f"http://product_service/products/{product_id}")
        if product_response.status_code != 200:
            return Response(product_response.json(), status=status.HTTP_400_BAD_REQUEST)

        cart, created = Cart.objects.get_or_create(user_id=user_id)
        item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        item.quantity += quantity
        item.save()

        return Response({'status': 'success', "user_id": user_id, 'item_id': item.product_id})

