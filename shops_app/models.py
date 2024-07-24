from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    avg_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_ratings = models.PositiveIntegerField(default=0)
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
    
    
class Review(models.Model):
    rating = models.DecimalField(max_digits=5, decimal_places=2, 
                                 validators=[MaxValueValidator(5),MinValueValidator(1)])
    text = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.text} - {self.rating}"
    

class ShopReview(models.Model):
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    text = models.CharField(max_length=500)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_reviews')
    review_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.text} - {self.rating}"



