import uuid
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, help_text="Name of department")
    uuid = models.UUIDField(unique=True, default=uuid.uuid4(), help_text="UUID of department")

    def __str__(self):
        return self.name
