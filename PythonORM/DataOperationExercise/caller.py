import os
from decimal import Decimal

import django
from django.db.models import When, Case, F, Value
from django.db.models.fields import PositiveIntegerField
from django.db.models.functions import Mod

from main_app.choices import RoomTypeChoices, ClassNameChoices

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Location, Car, Task, HotelRoom, Character
from main_app.models import Artifact

# Create queries within functions
def create_pet(name, species):
    Pet.objects.create(name=name, species=species)
    return f'{name} is a very cute {species}!'

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f'The artifact {name} is {age} years old!'


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age>250:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()

def show_all_locations():
    return '\n'.join(f"{l.name} has a population of {l.population}!" for l in Location.objects.all().order_by('-id'))

def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()

def get_capitals():
    return Location.objects.filter(is_capital=True)

def delete_first_location():
    Location.objects.first().delete()

def apply_discount():
    for car in Car.objects.all():
        discount = Decimal(str(sum(int(d) for d in str(car.year))/100)) * car.price
        car.price_with_discount = car.price - discount
        car.save()

def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')

def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(f"Task - {t.title} needs to be done until {t.due_date}!" for t in tasks)

def complete_odd_tasks():
    Task.objects.annotate(
        odd=Mod("id", 2)
    ).filter(odd=1).update(is_finished=True)

def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = ''
    for c in text:
        encoded_text += chr(ord(c) - 3)
    Task.objects.filter(title=task_title).update(description=encoded_text)

def get_deluxe_rooms():
    rooms = (HotelRoom.objects.
              annotate(even=Mod('id', 2)).filter(even=0).
              filter(room_type=RoomTypeChoices.DELUXE))
    return '\n'.join(f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!" for r in rooms)

def increase_room_capacity():
    reserved_rooms = HotelRoom.objects.filter(is_reserved=True).order_by('id')
    previous_room = None

    for r in reserved_rooms:
        if previous_room:
            r.capacity += previous_room.capacity
        else:
            r.capacity += r.id
        r.save()
        previous_room = r

def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()

def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()


def update_characters():
    Character.objects.update(
        level=Case(
            When(class_name=ClassNameChoices.MAGE, then=F('level') + 3),
            default=F('level')
        ),
        intelligence=Case(
            When(class_name=ClassNameChoices.MAGE, then=F('intelligence') + 5),
            default=F('intelligence')
        ),
        hit_points = Case(
            When(class_name=ClassNameChoices.WARRIOR, then=F('hit_points') / 2),
            default=F('hit_points')
        ),
        dexterity=Case(
            When(class_name=ClassNameChoices.WARRIOR, then=F('dexterity') + 4),
            default=F('dexterity')
        ),
        inventory = Case(
            When(class_name__in=[ClassNameChoices.ASSASSIN, ClassNameChoices.SCOUT], then=Value('The inventory is empty') ),
            default=F('inventory')
        )
    )

def fuse_characters(first_character: Character, second_character: Character) -> None:
    inventory = None

    if first_character.class_name in [ClassNameChoices.MAGE,ClassNameChoices.SCOUT]:
        inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    elif first_character.class_name in [ClassNameChoices.WARRIOR,ClassNameChoices.ASSASSIN]:
        inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name='Fusion',
        level=(first_character.level + second_character.level)//2,
        strength=int((first_character.strength + second_character.strength) * 1.2),
        dexterity=int((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=int((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory=inventory
    )
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)

def grand_intelligence():
    Character.objects.update(intelligence=40)

def grand_strength():
    Character.objects.update(strength=50)

def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()