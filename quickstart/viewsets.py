from rest_framework import viewsets
from . import models, serializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()

    # we have to use EmployeeSerializer for the json conversion
    serializer_class = serializer.EmployeeSerializer