from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,)

class Fruit(models.Model):
    name = models.CharField(max_length=30,
                            unique=True,
                            validators=[
                                MinLengthValidator(2),
                                RegexValidator(regex=r'^[a-zA-Z]+$', message="Fruit name should contain only letters!")
                            ])
    Image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)
category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fruits')