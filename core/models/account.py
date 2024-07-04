from django.contrib.auth.models import AbstractUser
from core.models.base import Base
from django.db import models


class Account(Base, AbstractUser):

    is_staff = models.BooleanField(name="is_staff", blank=False, null=False, default=False)
    is_active = models.BooleanField(name="is_active", blank=False, null=False, default=True)
    is_superuser = models.BooleanField(name="is_superuser", blank=False, null=False, default=False)
    email = models.EmailField(name="email", max_length=100, unique=True, blank=False, null=False, editable=True)
    condo = models.OneToOneField(to="Condo",
                                 name="condo",
                                 on_delete=models.CASCADE,
                                 related_name="account",
                                 editable=True,
                                 blank=False,
                                 null=False)

    phone = models.CharField(name="phone", max_length=11, blank=True, null=True, editable=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username', 'password', 'first_name',)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.email}"
