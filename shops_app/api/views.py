from rest_framework import generics

from shops_app.models import Shop, Product
from shops_app.api.serializers import ShopSerializer



class ShopListGV(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    

