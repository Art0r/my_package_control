from django.core.management.base import BaseCommand
from core.models import (Resident,
                         Account,
                         Apartment,
                         Condo)
from django.contrib.auth.hashers import make_password
from faker import Faker
import random
import os
import subprocess


class Command(BaseCommand):
    help = "seed database"

    @staticmethod
    def delete_db():
        if os.path.isfile("./db.sqlite3"):
            os.remove("./db.sqlite3")

    @staticmethod
    def delete_migration():
        if os.path.isfile("./core/migrations/0001_initial.py"):
            os.remove("./core/migrations/0001_initial.py")

    @staticmethod
    def migrate():
        subprocess.run(['python', 'manage.py', 'makemigrations'])
        subprocess.run(['python', 'manage.py', 'migrate'])

    def handle(self, *args, **options):
        self.delete_db()
        self.delete_migration()
        self.migrate()

        faker = Faker()

        condo = Condo.objects.create(number=77, street="Rua Coiso")

        account = Account.objects.create(
            email="art@art.com",
            password=make_password("123"),
            username="art",
            phone="1234123",
            condo=condo
        )

        for i in range(5):
            apto = Apartment.objects.create(
                number=int(round(random.random(), 4) * (10 ** 4)),
                floor=int(round(random.random(), 1) * (10 ** 1)),
                condo=condo
            )

        for i in range(10):
            random_apto = Apartment.objects.order_by('?').first()

            Resident.objects.create(
                name=faker.name(),
                email=faker.email(),
                phone=int(round(random.random(), 9) * (10 ** 9)),
                apto=random_apto  # Associate with a random apartment
            )
