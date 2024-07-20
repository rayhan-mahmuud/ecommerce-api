from django.db import models
from django.contrib.auth.models import User


PRODUCT_CATEGORIES = [
    ('electronics', 'Electronics'),
    ('fashion', 'Fashion'),
    ('home_garden', 'Home & Garden'),
    ('beauty_health', 'Beauty & Health'),
    ('sports_outdoors', 'Sports & Outdoors'),
    ('toys_games', 'Toys & Games'),
    ('automotive', 'Automotive'),
    ('books', 'Books'),
    ('music', 'Music'),
    ('groceries', 'Groceries')
]
    

class Shop(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    
    
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=25, choices=PRODUCT_CATEGORIES)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    


