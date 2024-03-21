from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100)
    recipe_desc = models.TextField(default='Default description')
    recipe_image = models.ImageField(upload_to="recipenew", default='Default image')