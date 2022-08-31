from django.db import models
from users.models import Account



# Create your models here.
class Post(models.Model) :
    owner = models.ForeignKey(Account, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    post_image = models.ImageField(upload_to="post_image", null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.content} - {self.owner.username}'