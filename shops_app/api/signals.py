from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from shops_app.models import ShopReview


# Updates the avg_rating and total ratings of the Shop model on creating of a new ShopReview 
@receiver(post_save, sender=ShopReview)
def update_ratings_on_shopreview_create(sender, instance, created, **kwargs):
    if created:
        total_rating_count = instance.shop.shop_reviews.count()
        
        previous_total = total_rating_count - 1
        previous_avg_rating = previous_total*instance.shop.avg_rating
        
        if total_rating_count != 0:
            avg_rating = (previous_avg_rating + instance.rating)/total_rating_count
        else:
            avg_rating = 0
        
        instance.shop.avg_rating = avg_rating
        instance.shop.total_ratings = total_rating_count
        
        instance.save()

       
# Updates the avg_rating and total ratings of the Shop model on deleting a ShopReview        
@receiver(post_delete, sender=ShopReview)
def update_ratings_on_shopreview_delete(sender, instance, **kwargs):
    total_rating_count = instance.shop.shop_reviews.count()
    
    previous_total = total_rating_count + 1
    previous_avg_rating = previous_total*instance.shop.avg_rating
    
    if total_rating_count != 0:
        avg_rating = (previous_avg_rating - instance.rating)/total_rating_count
    else:
        avg_rating = 0
    
    instance.shop.avg_rating = avg_rating
    instance.shop.total_ratings = total_rating_count
    
    instance.save()
    
    
