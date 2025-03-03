from django.shortcuts import render
from .models import Department

def department_tree(request):
    departments = Department.objects.prefetch_related('subdepartments', 'employee_set').all()
    return render(request, 'department_tree.html', {'departments': departments})
