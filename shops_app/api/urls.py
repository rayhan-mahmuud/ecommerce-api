from django.urls import path

from shops_app.api.views import ShopListGV


urlpatterns = [
    path("shops/", ShopListGV.as_view(), name='shops_list'),
]


