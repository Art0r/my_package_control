from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core.models import Resident, Apartment, Account
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

        condo = Account(
            type=Account.Types.CONDO,
            email="art@art.com",
            password="123",
            username="art"
        )

        condo.save()

        condo_staff = Account(
            type=Account.Types.CONDO_STAFF,
            email="ar1t@art1.com",
            password="123",
            username="art1"
        )

        condo_staff.save()

        for i in range(5):

            apto = Apartment()
            number = int(round(random.random(), 4) * (10 ** 4))
            floor = int(round(random.random(), 1) * (10 ** 1))

            apto.number = number
            apto.floor = floor

            apto.condo = condo
            apto.save()

        for i in range(10):

            random_apto = Apartment.objects.order_by('?').first()

            name = faker.name()
            email = faker.email()
            phone = int(round(random.random(), 9) * (10 ** 9))

            resident = Resident()

            resident.name = name
            resident.email = email
            resident.apto = random_apto
            resident.phone = phone

            resident.save()
            random_apto.save()
