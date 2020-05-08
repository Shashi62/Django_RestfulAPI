from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import EmployeeSerializer

# Create your views here.


class EmployeeList(APIView):

    def get(self, request):
        emp1 = Employee.objects.all()
        serializer = EmployeeSerializer(emp1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
