import os
from datetime import timedelta, date
import django
from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Song, Artist, Product, Review, DrivingLicense, Driver, Owner, Car, Registration
from django.db.models import Avg

def show_all_authors_with_their_books():
    authors = Author.objects.all()
    return '\n'.join(f"{a.name} has written - {', '.join(b.title for b in a.book_set.all())}!" for a in authors if a.book_set.exists())
def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()

def add_song_to_artist(artist_name: str, song_title: str):
    Artist.objects.get(name=artist_name).songs.add(Song.objects.get(title=song_title))

def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')

def remove_song_from_artist(artist_name: str, song_title: str):
    Artist.objects.get(name=artist_name).songs.remove(Song.objects.get(title=song_title))

def calculate_average_rating_for_product_by_name(product_name: str):
    return Product.objects.annotate(avg_review_score=Avg('reviews__rating')).get(name=product_name).avg_review_score

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)

def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()

def calculate_licenses_expiration_dates():
    return '\n'.join(f"License with number: {l.license_number} expires on {l.issue_date+timedelta(days=365)}!"
                     for l in DrivingLicense.objects.all().order_by('-license_number'))

def get_drivers_with_expired_licenses(due_date: date):
    expired_licenses = DrivingLicense.objects.filter(issue_date__lt=due_date - timedelta(days=365))
    return Driver.objects.filter(license__in=expired_licenses)

def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()
    registration.car = car
    registration.registration_date = timezone.now().date()
    registration.save()
    car.owner = owner
    car.save()
    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
































