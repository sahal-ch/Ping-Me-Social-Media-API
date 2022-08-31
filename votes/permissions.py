from rest_framework.permissions import BasePermission, SAFE_METHODS




class HasSelfVotedOrReadOnly(BasePermission):
    
    # Custom permission to only allow owners of an object to edit it.
    def has_object_permission(self, request, view, obj):
        
        # Will allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.up_vote_by == request.user or obj.down_vote_by==request.user