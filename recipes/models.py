from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    image = models.ImageField(upload_to='recipe_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    preparation_time = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class RecipeCategoryRelationship(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    

    class Meta:
        unique_together = ['recipe', 'category']