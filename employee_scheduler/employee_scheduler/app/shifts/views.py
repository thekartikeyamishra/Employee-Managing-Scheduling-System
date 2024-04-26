from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Shift
from .serializers import ShiftSerializer

class ShiftList(APIView):

  def get(self, request):
    from_date = request.GET.get('from', None)
    to_date = request.GET.get('to', None)
    if from_date and to_date:
      shifts = Shift.objects.filter(start_time__range=[from_date, to_date])
    else:
      shifts = Shift.objects.all()
    serializer = ShiftSerializer(shifts, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ShiftSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShiftDetail(APIView):
  """
  API endpoint to retrieve, update, or delete a shift.
  """
  def get_object(self, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return shift

  def get(self, request, pk):
    shift = self.get_object(pk)
    serializer = ShiftSerializer(shift)
    return Response(serializer.data)

  def put(self, request, pk):
    shift = self.get_object(pk)
    serializer = ShiftSerializer(shift, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    shift = self.get_object(pk)
    shift.delete()
