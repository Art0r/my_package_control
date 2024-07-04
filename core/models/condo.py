from core.models.base import Base
from django.db import models


class Condo(Base):

    number = models.IntegerField(name="number", blank=True, null=True, editable=True)
    street = models.CharField(name="street", blank=True, null=True, editable=True, max_length=64)

    def __str__(self) -> str:
        return f"{self.street}, {self.number}"
