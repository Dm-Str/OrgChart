from django.core.management.base import BaseCommand
from company_structure.models import Employee, Department
from faker import Faker
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')

        departments = []
        for i in range(25):
            department = Department.objects.create(name=f'Отдел {i + 1}')
            departments.append(department)
            if i > 0:
                department.parent = random.choice(departments[:i])
                department.save()

        employees = []
        for _ in range(50000):
            employees.append(Employee(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=random.uniform(30000, 120000),
                department=random.choice(departments)
            ))

        Employee.objects.bulk_create(employees)

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
