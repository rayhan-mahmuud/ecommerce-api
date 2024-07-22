from rest_framework import generics

from shops_app.models import Shop, Product, Review
from shops_app.api.serializers import ShopSerializer, ProductSerializer, ReviewSerializer



class ShopListView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)
    

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductReviewsList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        review_by = self.request.user
        serializer.save(review_by=review_by)
    

# class ShopReviewsList(generics.ListCreateAPIView):
#     queryset = ShopReview.objects.all()
#     serializer_class = ShopReviewSerializer
    
    
    