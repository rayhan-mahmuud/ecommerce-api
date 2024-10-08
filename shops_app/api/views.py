from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shops_app.models import Shop, Product, Review, ShopReview
from shops_app.api.serializers import ShopSerializer, ProductSerializer, ReviewSerializer, ShopReviewSerializer



class ShopListView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)
    

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    

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
    

class ShopReviewsList(generics.ListCreateAPIView):
    queryset = ShopReview.objects.all()
    serializer_class = ShopReviewSerializer
    
    def perform_create(self, serializer):
        review_by = self.request.user
        serializer.save(review_by=review_by)
    
    
    