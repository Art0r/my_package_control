import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Base(models.Model):
    id = models.UUIDField(name="id", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(name="created_at", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(name="updated_at", auto_now=True)

    class Meta:
        abstract = True


class Account(Base, AbstractUser):
    class Types(models.TextChoices):
        CONDO = "CONDO", "condo"
        CONDO_STAFF = "CONDO_STAFF", "condo_staff"

    type = models.CharField(max_length=11, choices=Types.choices, default=Types.CONDO_STAFF)
    is_staff = models.BooleanField(name="is_staff", blank=False, null=False, default=False)
    is_active = models.BooleanField(name="is_active", blank=False, null=False, default=True)
    is_superuser = models.BooleanField(name="is_superuser", blank=False, null=False, default=False)
    email = models.EmailField(name="email", max_length=100, unique=True, blank=False, null=False, editable=True)

    is_condo = models.BooleanField(name="is_condo", blank=False, null=False, default=False)
    is_condo_staff = models.BooleanField(name="is_condo_staff", blank=False, null=False, default=True)

    number = models.IntegerField(name="number", blank=True, null=True, editable=True)
    street = models.CharField(name="street", blank=True, null=True, editable=True, max_length=64)
    phone = models.CharField(name="phone", max_length=11, blank=True, null=True, editable=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username', 'password', 'first_name',)

    def save(self, *args, **kwargs):
        if not self.type or self.type is None:
            self.type = Account.Types.CONDO_STAFF

        if self.type == Account.Types.CONDO_STAFF:
            self.is_staff = False
            self.street = None
            self.number = None
            return super().save(*args, **kwargs)

        if self.type == Account.Types.CONDO:
            self.is_staff = True
            self.phone = None
            return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.email}"


class Apartment(Base):
    number = models.IntegerField(name="number", blank=False, null=False)
    floor = models.IntegerField(name="floor", blank=False, null=False)

    condo = models.ForeignKey(
        to="Account",
        related_name="apto",
        name="condo",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.condo.type is Account.Types.CONDO:
            return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.number}"


class Resident(Base):
    name = models.CharField(name="name", blank=False, null=False, max_length=64)
    email = models.EmailField(name="email", blank=False, null=False, max_length=64)
    phone = models.CharField(name="phone", blank=False, null=False, max_length=11)

    apto = models.ForeignKey(
        to="Apartment",
        name="apto",
        related_name="resident",
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.apto.number}"


class Package(Base):
    received = models.CharField(name="received", blank=True, null=True, max_length=128,
                                editable=False)
    retrieved = models.CharField(name="retrieved", blank=True, null=True, editable=True, max_length=128)
    retrieved_check = models.BooleanField(name="retrieved_check", blank=False, null=False, editable=True, default=False)

    resident = models.ForeignKey(to="Resident",
                                 name="resident",
                                 related_name="package",
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 editable=True)

    def __str__(self) -> str:
        return f"{self.id}"
