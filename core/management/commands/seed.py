from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core.models import Resident, Apartment
from faker import Faker
import random


class Command(BaseCommand):
    help = "seed database"

    def handle(self, *args, **options):
        faker = Faker()

        user = User(
            email="art@art.com",
            username="art",
            password="art",
            is_active=True,
            # is_staff=True,
            # is_superuser=True
        )

        user.save()

        token = Token(user=user)

        token.save()

        self.stdout.write(self.style.SUCCESS(token.key))

        for i in range(5):

            apto = Apartment()
            number = int(round(random.random(), 4) * (10 ** 4))
            floor = int(round(random.random(), 1) * (10 ** 1))

            apto.number = number
            apto.floor = floor

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



