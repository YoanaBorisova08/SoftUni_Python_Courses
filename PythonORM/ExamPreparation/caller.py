import os
from decimal import Decimal
import random

import django
from django.db.models import Q, Count, F

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
    if search_string is None:
        return ''
    searched_profiles = Profile.objects.filter(Q(full_name__icontains=search_string)
                           | Q(email__icontains=search_string)
                           | Q(phone_number__icontains=search_string)).prefetch_related('orders_per_user').order_by('full_name')
    if not searched_profiles.exists():
        return ''

    return '\n'.join(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.num_of_orders}" for p in searched_profiles.annotate(num_of_orders=Count('orders_per_user')))


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    if not profiles:
        return ''
    return '\n'.join(f"Profile: {p.full_name}, orders: {p.count_orders}" for p in profiles)

def get_last_sold_products():
    last_order = Order.objects.order_by('-creation_date').first()
    if not last_order:
        return ''
    products = last_order.products.order_by('name')
    if not products:
        return ''
    return f"Last sold products: {', '.join(p.name for p in products)}"

def get_top_products():
    top_products = Product.objects.annotate(num_of_orders=Count('orders')).order_by('-num_of_orders', 'name')[:5]
    if not top_products.exists():
        return ''
    lines = "\n".join(
        f"{p.name}, sold {p.num_of_orders} times"
        for p in top_products
    )

    return f"Top products:\n{lines}"

def apply_discounts():
    orders_with_discount = Order.objects.annotate(product_count=Count('products')).filter(product_count__gt=2, is_completed=False).update(total_price=F('total_price')*1.1)
    return f"Discount applied to {orders_with_discount} orders."

def complete_order():
    first_not_completed_order = Order.objects.filter(is_completed=False).order_by('-creation_date').first()
    if not first_not_completed_order:
        return ''
    first_not_completed_order.is_completed=True
    first_not_completed_order.save()
    products = list(first_not_completed_order.products.all())
    for p in products:
        p.in_stock-=1
        if p.in_stock==0:
            p.is_available=False
    Product.objects.bulk_update(
        products,
        ['in_stock', 'is_available']
    )

    return "Order has been completed!"
