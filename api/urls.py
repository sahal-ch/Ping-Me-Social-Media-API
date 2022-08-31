from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserRegisterViewSet
from user_profile.views import ProfileViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet
from votes.views import VoteViewSet
from friends.views import FollowingViewSet

from rest_framework_simplejwt import views as jwt_views
from django.urls import path



urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('register', UserRegisterViewSet, basename='register')
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('following', FollowingViewSet, basename='following')
router.register('posts', PostViewSet, basename='posts')
router.register('votes', VoteViewSet, basename='votes')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns += router.urls