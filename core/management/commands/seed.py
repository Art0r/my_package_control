from django.core.management.base import BaseCommand
from core.models import Resident, Apartment
from faker import Faker
import random


class Command(BaseCommand):
    help = "seed database"

    def handle(self, *args, **options):
        faker = Faker()

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

            resident = Resident()

            resident.name = name
            resident.email = email
            resident.apto = random_apto

            resident.save()
            random_apto.save()



