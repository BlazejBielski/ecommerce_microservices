from rest_framework import serializers
from django.db import transaction

from products.models import Category, Subcategory, CategoryProduct, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ("id", "name")


class CategoryWithSubcategoriesSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "subcategories")


class CategoryProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        models = CategoryProduct
        fields = ("id", "category_id", "product_id")


class CategoryWithoutProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = CategoryProduct
        fields = ("id", "category_id", "product_id")


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image",
            "popularity",
            "rank",
            "barcode",
            "stock_count",
            "categories",
            "subcategories",
        )

    def save(self, **kwargs):
        if "categories" in self.validated_data:
            self.data.categories = self.validated_data.pop("categories")

            return super().save(**kwargs)


class AddProductWithCategoriesAndSubcategoriesSerializer(serializers.ModelSerializer):
    categories = CategoryProductSerializer(source="categoryproduct_set", read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "popularity",
            "rank",
            "barcode",
            "categories",
            "stock_count",
            "description",
            "image",
        )

    @transaction.atomic
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        if "categories" in self.initial_data:
            categories = self.initial_data.get("categories")
            category_ids = [int(category_id.strip()) for category_id in categories.split(",")]
            for category_id in category_ids:
                category = Category.objects.get(pk=category_id)
                CategoryProduct.objects.create(category_id=category, product_id=product)

            if "subcategories" in self.initial_data:
                subcategories = self.initial_data.get("subcategories")
                subcategory_ids = [int(subcategory_id) for subcategory_id in subcategories.split(",")]

                for subcategory_id in subcategory_ids:
                    subcategory = Subcategory.objects.get(pk=subcategory_id)
                    product.subcategories.add(subcategory)

            product.save()
            return product
