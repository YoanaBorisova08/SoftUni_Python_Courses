import os
from decimal import Decimal
import random

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Order, Profile, Product

def populate_db():
    NAMES = [
        "John Smith", "Emily Johnson", "Michael Brown", "Sarah Davis",
        "Daniel Wilson", "Olivia Martinez", "James Anderson", "Sophia Taylor",
        "William Moore", "Emma Thompson"
    ]

    ADDRESSES = [
        "742 Evergreen Terrace, Springfield",
        "221B Baker Street, London",
        "1600 Pennsylvania Avenue NW, Washington",
        "10 Downing Street, London",
        "350 Fifth Avenue, New York",
        "4059 Mt Lee Drive, Hollywood",
        "31 Spooner Street, Quahog",
        "124 Conch Street, Bikini Bottom",
        "12 Grimmauld Place, London",
        "4 Privet Drive, Little Whinging"
    ]

    PRODUCTS = [
        ("Wireless Mouse", "Ergonomic wireless mouse"),
        ("Mechanical Keyboard", "RGB mechanical keyboard with blue switches"),
        ("USB-C Charger", "Fast charging 65W USB-C charger"),
        ("Bluetooth Headphones", "Noise-cancelling over-ear headphones"),
        ("Laptop Stand", "Adjustable aluminum laptop stand"),
        ("Smart Watch", "Fitness tracking smart watch"),
        ("External SSD", "1TB portable external SSD"),
        ("Webcam", "Full HD USB webcam"),
        ("Gaming Chair", "Ergonomic chair with lumbar support"),
        ("Portable Speaker", "Waterproof Bluetooth speaker"),
    ]

    # ---------- PROFILES ----------
    profiles = []
    for i in range(10):
        profile = Profile.objects.create(
            full_name=NAMES[i],
            email=f"{NAMES[i].lower().replace(' ', '.')}@example.com",
            phone_number=f"+35988877{i:02d}",
            address=ADDRESSES[i],
            is_active=True
        )
        profiles.append(profile)

    # ---------- PRODUCTS ----------
    products = []
    for name, description in PRODUCTS:
        product = Product.objects.create(
            name=name,
            description=description,
            price=Decimal(f"{random.randint(20, 300)}.99"),
            in_stock=random.randint(1, 100),
            is_available=True
        )
        products.append(product)

    # ---------- ORDERS ----------
    for _ in range(10):
        chosen_products = random.sample(products, k=random.randint(1, 4))
        total_price = sum(p.price for p in chosen_products)

        order = Order.objects.create(
            profile=random.choice(profiles),
            total_price=total_price,
            is_completed=random.choice([True, False])
        )

        order.products.set(chosen_products)

def get_profiles(search_string=None):
    