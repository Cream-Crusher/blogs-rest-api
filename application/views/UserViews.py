from rest_framework import generics
from application.serializers.UserSerializer import UserSerializer

from application.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
