from unicodedata import name
from .models import Post
from .serializers import PostSerializer
from user_profile.permissions import IsOwnerOrReadOnly
from friends.models import FriendRequest
from users.models import Account
from user_profile.models import UserProfile


from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action



# Create your views here.
class PostViewSet(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def perform_create(self, serializer) :
        serializer.save(owner=self.request.user)
        
    def list(self, request) :
        user=self.request.user.pk
        following = FriendRequest.objects.filter(request_from=user, status=True)
        result = [user]
        
        for i in range(len(following.values())) :
            result.append(following.values()[i]['request_to_id'])
            
        accounts = Account.objects.filter(id__in=result).values()
        
        for i in range(len(accounts.values())) :
            result.append(accounts.values()[i]['id'])
        
        queryset = Post.objects.filter(owner__in=result).order_by('-post_date')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
        
    @action(detail=False,methods=['GET'], name='Posts from other Accounts')
    def post_from_other_accounts(self,request):
        user = self.request.user.pk
        following = FriendRequest.objects.filter(request_from=user,status=True)
        result=[user]
        
        for i in range(len(following.values())):
            result.append(following.values()[i]['request_to_id'])
        account=Account.objects.exclude(id__in=result).values()
        result.clear()
        
        for i in range(len(account.values())):
            result.append(account.values()[i]['id'])
        users = UserProfile.objects.filter(is_private=False, owner__in=result)
        result.clear()
        
        for i in range(len(users.values())):
            result.append(users.values()[i]['owner_id'])
            
        post=Post.objects.filter(owner__in = result)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)