from django.db import models


class Review(models.Model):
    user_id = models.UUIDField(help_text="User id from auth service")
    product_id = models.IntegerField(help_text="Product id from product service")
    rating = models.PositiveIntegerField(help_text="Rating out of 5")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.product_id} review by {self.user_id}"
