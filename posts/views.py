from unicodedata import name
from .models import Post
from .serializers import PostSerializer
from user_profile.permissions import IsOwnerOrReadOnly
from friends.models import FriendRequest
from users.models import Account


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
        user=self.request.user.pk
        q1=FriendRequest.objects.filter(request_from=user,status=True)
        q2=FriendRequest.objects.filter(request_to=user,status=True)
        result=[]
        if q1.exists and not q2.exists:
            for i in range(len(q1.values())):
                result.append(q1.values()[i]['request_to_id'])
        elif not q1.exists and q2.exists:
            for i in range(len(q2.values())):
                result.append(q2.values()[i]['request_from_id'])
        elif q1.exists and q2.exists:
            for i in range(len(q1.values())):
                result.append(q1.values()[i]['request_to_id'])
            for i in range(len(q2.values())):
                result.append(q2.values()[i]['request_from_id'])
        else:
            pass     
        queryset = Post.objects.filter(owner__in=result).order_by('-post_date')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)