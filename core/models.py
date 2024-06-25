import uuid
from django.db import models


class Base(models.Model):
    id = models.UUIDField(name="id", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(name="created_at", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(name="updated_at", auto_now=True)

    class Meta:
        abstract = True


class Apartment(Base):
    number = models.IntegerField(name="number", blank=False, null=False)
    floor = models.IntegerField(name="floor", blank=False, null=False)


class Resident(Base):
    name = models.CharField(name="name", blank=False, null=False, max_length=64)
    email = models.EmailField(name="email", blank=False, null=False, max_length=64)

    apto = models.ForeignKey(to="Apartment", name="apto", related_name="resident",
                             blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.apto.number}"


class Package(Base):
    resident = models.ForeignKey(to="Resident", name="resident", related_name="package",
                                 blank=True, null=True, on_delete=models.CASCADE, editable=True)
    received = models.CharField(name="received", blank=True, null=True, max_length=128,
                                editable=False)
    retrieved = models.CharField(name="retrieved", blank=True, null=True, editable=True, max_length=128)
    retrieved_check = models.BooleanField(name="retrieved_check", blank=False, null=False, editable=True, default=False)



