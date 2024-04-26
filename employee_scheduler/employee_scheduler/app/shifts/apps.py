from django.apps import AppConfig

class ShiftsConfig(AppConfig):
  name = 'shifts'
  verbose_name = 'Shifts'

  def ready(self):
    pass
