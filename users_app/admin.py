from django.contrib import admin
from users_app.models import User, ShopOwner, Customer


admin.site.register(User)
admin.site.register(ShopOwner)
admin.site.register(Customer)
