import os
from datetime import date

import django
from django.db import connection

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing, VideoGame, Invoice, BillingInfo, Project, Programmer, Technology, Task, \
    Exercise
