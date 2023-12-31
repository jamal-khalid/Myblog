from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField( max_length=200)
    author=models.CharField(max_length=100)
    views=models.IntegerField(default=0)
    slug =models.CharField(max_length=50)
    time_stamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title +' from '+self.author
    
class BlogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    post=models.ForeignKey(Post ,on_delete=models.CASCADE)
    parent=models.ForeignKey('self' ,on_delete=models.CASCADE , null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment+" by "+self.user.username


    