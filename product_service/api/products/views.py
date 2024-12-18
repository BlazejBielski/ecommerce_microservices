from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from products.models import Category
from products.paginators import CustomPaginator
from products.serialziers import CategorySerializer, CategoryWithSubcategoriesSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPaginator
    permission_classes = (AllowAny,)


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)


class CategoryWithSubcategoriesRetrieveView(RetrieveAPIView):
    serializer_class = CategoryWithSubcategoriesSerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
