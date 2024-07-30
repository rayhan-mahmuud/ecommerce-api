# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth.models import User
# from users_app.api.serializers import UserSerializer

# class RegisterView(generics.CreateAPIView):
#     serializer_class = UserSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save()
            
#             refresh = RefreshToken.for_user(user)
#             data = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             }
            
#             return Response(data=data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        