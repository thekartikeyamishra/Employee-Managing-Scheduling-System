from .availability_manager import AvailabilityManager  

class DynamicScheduler:

    def __init__(self, employee_availability_manager):
        self.availability_manager = employee_availability_manager

    def schedule_employees(self, predicted_traffic, required_skills):
        available_employees = self.availability_manager.get_available_employees(required_skills)
        assigned_employees = random.sample(available_employees, int(predicted_traffic * 0.5))
        return assigned_employees
