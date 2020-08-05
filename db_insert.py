import csv
import os
import django
import sys

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_reminder.settings")
django.setup()

from stores.models import Store, Menu

with open("./stores.csv", newline="") as data:
    rows = csv.DictReader(data)

    for row in rows:
        Store.objects.create(
            name=row["name"],
            description=row["description"],
            address=row["address"],
            phone_number=row["phone_number"],
        )

with open("./menus.csv", newline="") as data:
    rows = csv.DictReader(data)

    for row in rows:
        Menu.objects.create(
            name=row["name"],
            store=Store.objects.get(id=row["store_id"]),
            price=row["price"],
        )
