from django_filters import FilterSet

from products.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
                  "price": ["gt", "lt", "gte", "lte"],
                  "name": ["exact"]
                  }
