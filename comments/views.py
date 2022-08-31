from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
from user_profile.permissions import IsOwnerOrReadOnly




# Create your views here.
class CommentViewSet(viewsets.ModelViewSet) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)