from django.db import models

# Create your models here.
class Contact(models.Model):
    sn=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=150)
    content=models.TextField()
    time_stamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'messages from '+self.name




