from django.core.management.base import BaseCommand
from core.models import Resident
from faker import Faker
import random


class Command(BaseCommand):
    help = "seed database"

    def handle(self, *args, **options):
        faker = Faker()

        for i in range(10):

            apto = int(round(random.random(), 4) * (10 ** 4))
            name = faker.name()
            email = faker.email()

            resident = Resident()

            resident.name = name
            resident.email = email
            resident.apto = apto

            resident.save()



