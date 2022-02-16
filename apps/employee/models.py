from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=100, help_text="Name of employee")

    def __str__(self):
        return self.employee_name
