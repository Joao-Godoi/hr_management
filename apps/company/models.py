import uuid
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=100, help_text="Name of company")
    company_uuid = models.UUIDField(default=uuid.uuid4(), unique=True, help_text="UUID of company")

    def __str__(self):
        return self.company_name
