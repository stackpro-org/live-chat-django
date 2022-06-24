from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="user", default="user/user.png")
    bio = models.TextField(null=True, blank=True)
   

    def __str__(self):
       
        if self.first_name and self.last_name:
            name=  str(f"{self.first_name} {self.last_name}")
        else:
            name = str(self.user.username)

        return name
    


class Chat(models.Model):
    content = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ManyToManyField(User)


