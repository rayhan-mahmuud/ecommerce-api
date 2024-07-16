from rest_framework import serializers

from shops_app.models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shop
        fields = '__all__'
    

