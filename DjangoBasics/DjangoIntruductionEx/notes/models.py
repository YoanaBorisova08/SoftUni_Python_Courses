from django.db import models

import categories.models
from categories.models import Category
from notes.choices import PriorityChoices


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PriorityChoices)
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, related_name='notes',
                                 blank=True, null=True)

    def __str__(self):
        return self.title

