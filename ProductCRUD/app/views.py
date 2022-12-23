from django.utils.decorators import method_decorator

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet

from .models import (
    CategoryModel,
    ProductModel
)
from .serializers import (
    CategorySerializer,
    ProductSerializer
)

# Create your views here.
@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="List of products",
    ),
)
@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_summary="Add category",
    ),
)
class CategoryListView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all().order_by('id')
    serializer_class = CategorySerializer


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="List of Products",
    ),
)
@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_summary="Add new Product",
    ),
)
class ProductListView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all().order_by('code')
    serializer_class = ProductSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary='Get Product by id',
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_summary="Update Product",
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Delete Product",
    )
)
class ProductDetailView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'put', 'delete']