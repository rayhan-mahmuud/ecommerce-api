from django.contrib import admin

from shops_app.models import Shop, Product, Review, ShopReview


admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ShopReview)
