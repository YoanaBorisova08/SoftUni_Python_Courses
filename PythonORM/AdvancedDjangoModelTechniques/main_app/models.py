from decimal import Decimal

from django.contrib.postgres.search import SearchVectorField
from django.core.validators import MinValueValidator, EmailValidator, RegexValidator, URLValidator, MinLengthValidator
from django.db import models

from main_app.validators import NameValidator


class Customer(models.Model):
    name = models.CharField(max_length=100,
                            validators=[
                                NameValidator('Name can only contain letters and spaces')
                            ],
                            )

    age = models.PositiveIntegerField(validators=[
        MinValueValidator(18, 'Age must be greater than or equal to 18'),
    ])

    email = models.EmailField(
        error_messages = {'invalid': 'Enter a valid email address'},
    )

    phone_number = models.CharField(max_length=13,
                                    validators=[
                                        RegexValidator(r'^\+359[0-9]{9}$', "Phone number must start with '+359' followed by 9 digits"),
                                    ])

    website_url = models.URLField(
        error_messages={'invalid':'Enter a valid URL'},
    )

class BaseMedia(models.Model):
    title = models.CharField(max_length=100,)
    description = models.TextField()
    genre = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

class Book(BaseMedia):
    author = models.CharField(max_length=100,
                              validators=[
                                  MinLengthValidator(5, 'Author must be at least 5 characters long'),
                              ])
    isbn = models.CharField(max_length=20,
                            validators=[
                                MinLengthValidator(6, 'ISBN must be at least 6 characters long')
                                ])
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

class Movie(BaseMedia):
    director = models.CharField(max_length=100,
                                validators=[
                                    MinLengthValidator(8, 'Director must be at least 8 characters long')
                                ])
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

class Music(BaseMedia):
    artist = models.CharField(max_length=100,
                              validators=[
                                  MinLengthValidator(9, 'Artist must be at least 9 characters long')
                              ])
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    TAX_MULTIPLIER = Decimal('0.08')
    SHIPPING_MULTIPLIER = Decimal('2')
    name = models.CharField(max_length=100,)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    @property
    def class_name(self):
        return 'Product'

    def calculate_tax(self):
        return self.TAX_MULTIPLIER * self.price


    def calculate_shipping_cost(self, weight: Decimal):
        return self.SHIPPING_MULTIPLIER * weight

    def format_product_name(self):
        return f"{self.class_name}: {self.name}"

class DiscountedProduct(Product):
    TAX_MULTIPLIER = Decimal('0.05')
    SHIPPING_MULTIPLIER = Decimal('1.5')

    @property
    def class_name(self):
        return 'Discounted Product'

    def calculate_price_without_discount(self):
        return self.price * Decimal('1.2')


    class Meta:
        proxy = True

class RechargeEnergyMixin(models.Model):
    energy = models.PositiveIntegerField()
    def recharge_energy(self, amount: int):
        self.energy = min(100, self.energy + amount)

class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100,)
    hero_title = models.CharField(max_length=100,)

class SpiderHero(Hero):
    def swing_from_buildings(self):
        if self.energy<80:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        self.energy -= 80
        if self.energy == 0:
            self.energy = 1
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True

class FlashHero(Hero):
    def run_at_super_speed(self):
        if self.energy<65:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        self.energy -= 65
        if self.energy == 0:
            self.energy = 1
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True


class Document(models.Model):
    title = models.CharField(max_length=200,)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['search_vector']),
        ]
