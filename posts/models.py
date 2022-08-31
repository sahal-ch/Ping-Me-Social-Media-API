from django.db import models
from users.models import Account



# Create your models here.
class Post(models.Model) :
    owner = models.ForeignKey(Account, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    post_media = models.FileField(upload_to="post/post_media")
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.content} - {self.owner.username}'