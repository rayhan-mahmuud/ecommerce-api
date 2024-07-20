from django.urls import path

from shops_app.api.views import ShopListView, ShopDetailView, ProductDetailView, ProductListView


urlpatterns = [
    path("shops/", ShopListView.as_view(), name='shops_list'),
    path("shops/<int:pk>/", ShopDetailView.as_view(), name='shops_detail'),
    path("products/", ProductListView.as_view(), name='product_list' ),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
    
    
]


