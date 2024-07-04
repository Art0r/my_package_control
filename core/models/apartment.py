from core.models.account import Account
from core.models.base import Base
from django.db import models


class Apartment(Base):
    number = models.IntegerField(name="number", blank=False, null=False)
    floor = models.IntegerField(name="floor", blank=False, null=False)

    condo = models.ForeignKey(
        to="Condo",
        related_name="apto",
        name="condo",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.number}"
