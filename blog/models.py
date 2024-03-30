from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


# Create your models here.
class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=255)
    Content = models.TextField()
    Image = models.ImageField(upload_to='Blog/Images', default='default.jpg')
    Category = models.ManyToManyField(Category)
    Tags = models.IntegerField(default=0)
    Counted_Views = models.IntegerField(default=0)
    Status = models.BooleanField(default=True)
    Publish_date = models.DateField()
    Publish_time = models.TimeField(default="00:00:00")
    Created_date = models.DateField(auto_now_add=True)
    Updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Title
