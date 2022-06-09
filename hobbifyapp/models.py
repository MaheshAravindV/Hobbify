from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name + " " + self.description
    hobby_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Likes(models.Model):
    def __str__(self):
        return self.liker.username + " likes " + self.likee.username
    liker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liker")
    likee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likee")
