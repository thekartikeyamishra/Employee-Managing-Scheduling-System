from django.apps import AppConfig

class EmployeesConfig(AppConfig):
  name = 'employees'
  verbose_name = 'Employees'

  def ready(self):
    pass
