from rest_framework import generics

from shops_app.models import Shop, Product
from shops_app.api.serializers import ShopSerializer, ProductSerializer



class ShopListView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    