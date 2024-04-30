from django.db import models


# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255, blank=True)
    Email = models.EmailField()
    Message = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('Created_date',)
