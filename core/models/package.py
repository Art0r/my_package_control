from core.models.base import Base
from django.db import models


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
