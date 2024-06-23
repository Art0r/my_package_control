import uuid

from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Resident(Base):
    apto = models.IntegerField(name="apto", blank=False, null=False)
    name = models.CharField(name="name", blank=False, null=False, max_length=64)
    email = models.EmailField(name="email", blank=False, null=False, max_length=64)