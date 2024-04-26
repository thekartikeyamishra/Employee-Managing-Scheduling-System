from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeList(APIView):
  
  def get(self, request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
  """
  API endpoint to retrieve, update, or delete an employee.
  """
  def get_object(self, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return employee

  def get(self, request, pk):
    employee = self.get_object(pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

  def put(self, request, pk):
    employee = self.get_object(pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    employee = self.get_object(pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
