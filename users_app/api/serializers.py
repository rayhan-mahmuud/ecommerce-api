from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group

from users_app.models import User, ShopOwner, Customer


class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        role = validated_data['role']
        
        if role == User.Roles.CUSTOMER:
            user = Customer.objects.create(
                username=username,
                email=email,
                role=role
            )
        elif role == User.Roles.SHOP_OWNER:
            user = ShopOwner.objects.create(
                username=username,
                email=email,
                role=role
            )
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                role=role
            )
        user.set_password(password)
        user.save()
        return user
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role' ]
        
    