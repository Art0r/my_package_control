from core.models.base import Base
from django.db import models


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
