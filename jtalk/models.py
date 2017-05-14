from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.username

class Review(models.Model):
    author = models.ForeignKey(User)
    score = models.IntegerField(null=True, blank=True)