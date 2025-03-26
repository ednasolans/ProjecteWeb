from django.db import models

# Create your models here.


class Receptes(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    name_recipe = models.CharField(max_length=120)
    description_recipe = models.TextField()
    instructions_recipe = models.TextField()
    image_recipe = models.ImageField(upload_to='recipe_images')
    source = models.CharField(max_length=120)

    def __str__(self):
        return self.name_recipe