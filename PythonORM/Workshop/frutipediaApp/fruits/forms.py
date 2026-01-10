from django import forms
from .models import Fruit, Category


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

class FruitCreateForm(FruitBaseForm):
    pass

class FruitEditForm(FruitBaseForm):
    pass

class FruitDeleteForm(FruitBaseForm):
    pass

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryCreateForm(CategoryBaseForm):
    pass