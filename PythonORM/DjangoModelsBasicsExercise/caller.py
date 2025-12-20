import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Recipe

recipe = Recipe(
    name = "sandwich",
    description = "A delicious sandwich",
    ingredients = "bread, ham, cheese, lettuce, tomato",
    cook_time = 10
)
recipe.save()