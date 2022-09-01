from django.db import models
from users.models import Account


# Create your models here.
class UserProfile(models.Model) :
    is_private = models.BooleanField(default=False)
    owner = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile_data')
    phone = models.CharField(max_length=12, null=True, blank=True)
    works_at = models.CharField(max_length=255, null=True, blank=True)
    lives_in = models.CharField(max_length=255, null=True, blank=True)
    studies_at = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
    
    def __str__(self) :
        return self.owner.username