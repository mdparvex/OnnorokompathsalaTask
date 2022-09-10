from email.policy import default
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):

    def __str__(self):
        return str(self.email)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    postdescription = models.TextField()
    video_link = models.CharField(max_length=300)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

class Like(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

class Dislike(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

