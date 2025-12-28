from django.db import models


class RoomTypeChoices(models.TextChoices):
    STANDARD = 'Standard', 'Standard'
    DELUXE = 'Deluxe', 'Deluxe'
    SUITE = 'Suite', 'Suite'

class ClassNameChoices(models.TextChoices):
    WARRIOR = 'Warrior', 'Warrior'
    MAGE = 'Mage', 'Mage'
    ASSASSIN = 'Assassin', 'Assassin'
    SCOUT = 'Scout', 'Scout'
