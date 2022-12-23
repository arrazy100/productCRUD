from django.urls.conf import path

from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView
)

urlpatterns = [
    path(
        'category',
        CategoryListView.as_view(),
        name='category'
    ),
    path(
        'product',
        ProductListView.as_view(),
        name='product'
    ),
    path(
        'product/<int:pk>',
        ProductDetailView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        }),
        name='product_detail'
    )
]