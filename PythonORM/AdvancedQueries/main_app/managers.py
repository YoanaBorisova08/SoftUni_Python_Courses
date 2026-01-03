from decimal import Decimal

from django.db import models
from django.db.models.aggregates import Count, Avg

from main_app.querysets import RealEstateQuerySet, VideoGameQuerySet


class RealEstateListingManager(models.Manager.from_queryset(RealEstateQuerySet)):
    def popular_locations(self):
        return self.values('location').annotate(location_count=Count('location')).order_by('-location_count', 'location')[:2]


class VideoGameManager(models.Manager.from_queryset(VideoGameQuerySet)):
    def highest_rated_game(self):
        return self.order_by('-rating').first()

    def lowest_rated_game(self):
        return self.order_by('rating').first()

    def average_rating(self):
        avg_rating = self.aggregate(avg=Avg('rating'))['avg']
        return f"{avg_rating:.1f}"
