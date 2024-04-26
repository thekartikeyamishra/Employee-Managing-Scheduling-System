from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    available_weekdays = models.CharField(max_length=7, blank=True)  # e.g., "MTWTF"
    available_from = models.TimeField(blank=True, null=True)
    available_to = models.TimeField(blank=True, null=True)

    skills = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
