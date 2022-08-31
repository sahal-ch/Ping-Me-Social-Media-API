from rest_framework import viewsets, permissions, serializers
from .models import Vote
from .serializers import VoteSerializer
from .permissions import HasSelfVotedOrReadOnly
from django.shortcuts import get_object_or_404
from posts.models import Post




# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset=Vote.objects.all()
    serializer_class=VoteSerializer
    permission_classes=[permissions.IsAuthenticated,HasSelfVotedOrReadOnly]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post'])

        #if user likes the post
        if self.request.data['vote']:
            already_up_voted=Vote.objects.filter(post=post_instance,up_vote_by=self.request.user).first()
            if already_up_voted:
                raise serializers.ValidationError({"message":"You have already liked this post"})
            else:
                
                # Deleting the dislike vote if it exists.
                already_down_voted=Vote.objects.filter(post=post_instance,down_vote_by=self.request.user).first()
                if already_down_voted :
                    already_down_voted.delete()
                serializer.save(up_vote_by=self.request.user,post=post_instance)
        #if user dislikes the post
        else:
            already_down_voted=Vote.objects.filter(post=post_instance,down_vote_by=self.request.user).exists()
            if already_down_voted:
                raise serializers.ValidationError({"message":"You have already disliked this post"})
            else:
                
                # Deleting the like vote if it exists.
                already_up_voted=Vote.objects.filter(post=post_instance,up_vote_by=self.request.user).exists()
                if already_up_voted :
                    already_up_voted.delete()
                serializer.save(down_vote_by=self.request.user,post=post_instance)
        
            