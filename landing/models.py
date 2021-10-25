from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    views = models.IntegerField()

class Board(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

class Pin(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    website = models.CharField(max_length=200)
    alt_text = models.TextField()
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    pin_id = models.ForeignKey(Pin, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

class Favorite(models.Model):
    pin_id = models.ForeignKey(Pin, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




