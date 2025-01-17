import uuid

from django.db import models

from cart.utils import TimeStampModel, OwnerModel


class Cart(TimeStampModel, OwnerModel):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
