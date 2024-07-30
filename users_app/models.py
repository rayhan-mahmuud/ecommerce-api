from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        SHOP_OWNER = "SHOP_OWNER", 'Shop Owner'
        CUSTOMER = "CUSTOMER", 'Customer'
    
    base_role = Roles.ADMIN
    role = models.CharField(max_length=20, choices=Roles.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)    

class ShopOwnerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.SHOP_OWNER)
    
class ShopOwner(User):
    
    base_role = User.Roles.SHOP_OWNER
    objects = ShopOwnerManager()
    
    class Meta:
        proxy = True
        

class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.CUSTOMER) 

class Customer(User):
    
    base_role = User.Roles.CUSTOMER
    objects = CustomerManager()
    
    class Meta:
        proxy = True
    

    
        
