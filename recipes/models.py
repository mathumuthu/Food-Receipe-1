from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    category = models.CharField(max_length=50)
