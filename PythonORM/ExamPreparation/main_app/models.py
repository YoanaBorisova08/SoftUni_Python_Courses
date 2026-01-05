from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import ProfileManager


class TimeStampModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Profile(TimeStampModel):
    full_name = models.CharField(max_length=100,
                                 validators=[
                                     MinLengthValidator(2),
                                     MaxLengthValidator(100)
                                 ])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    objects = ProfileManager()


class Product(TimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10,
                                validators=[
                                    MinValueValidator(0.01)
                                ])
    in_stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)

class Order(TimeStampModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders_per_user')
    products = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)])
    is_completed = models.BooleanField(default=False)