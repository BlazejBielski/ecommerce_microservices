from django.db import models
from django.utils.text import slugify

from products.utils import OwnerModel, TimeStampModel


class Product(TimeStampModel, OwnerModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    slug = models.SlugField(blank=True, max_length=255, unique=True)
    popularity = models.PositiveIntegerField(default=0, help_text="Incrementation when user sees details page.")
    sales_count = models.PositiveIntegerField(default=0)
    barcode = models.CharField(max_length=13, blank=True)
    rank = models.IntegerField(help_text="Rank from review service")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.full_clean()
        super().save(*args, **kwargs)
