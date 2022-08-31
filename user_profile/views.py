from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated




# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer) :
        serializer.save(owner=self.request.user)
        