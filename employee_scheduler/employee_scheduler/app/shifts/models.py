from django.db import models
from django.utils import timezone

class Shift(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    department = models.CharField(max_length=50)
    required_skills = models.CharField(max_length=255)
    assigned_employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.department} Shift - {self.start_time} to {self.end_time}"

    def is_overlapping(self, other_shift):
        return (self.start_time < other_shift.end_time) and (self.end_time > other_shift.start_time)

    def is_available(self, employee):
        if not employee.available_weekdays:
            return False  
        weekday = self.start_time.strftime("%w")  
        return (weekday in employee.available_weekdays) and (employee.available_from <= self.start_time <= employee.available_to) and (employee.available_from <= self.end_time <= employee.available_to) and (employee.skills.find(self.required_skills) != -1)
