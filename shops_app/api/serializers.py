from rest_framework import serializers

from shops_app.models import Shop, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    review_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        
# class ShopReviewSerializer(serializers.ModelSerializer):
    
#     review_by = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = ShopReview
#         fields = '__all__'
        


class ProductSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'



class ShopSerializer(serializers.ModelSerializer):
    
    # reviews = ShopReviewSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Shop
        fields = '__all__'
    

