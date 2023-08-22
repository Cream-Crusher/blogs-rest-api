from rest_framework import generics
from application.serializers.UserSerializer import UserSerializer, UserSerializerСhanges
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from application.models import User


class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializerСhanges
