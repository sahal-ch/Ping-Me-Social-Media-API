from django.db import models
from users.models import Account
from posts.models import Post




# Create your models here.
class Comment(models.Model) :
    owner = models.ForeignKey(Account, on_delete=models.Case)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment=models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_edited = models.DateField(auto_now=True)
    
    def __str__(self) :
        return f'{self.comment} - {self.owner.username}'