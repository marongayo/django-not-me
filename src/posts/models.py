from os import name
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ManyToManyField, OneToOneField
user = get_user_model


# Create your models here.
class Author(models.Model):
    user = OneToOneField(user, on_delete= models.CASCADE)
    profile_image = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    commentCount = models.IntegerField(default=0)
    thumnail = models.ImageField()
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    category = ManyToManyField(Category)

    def __str__(self):
        return self.title