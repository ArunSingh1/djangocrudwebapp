from rest_framework import viewsets
from . import models
from . import serializers

class CarsViewset(viewsets.ModelViewSet):
    queryset = models.Cars.objects.all()
    serializer_class = serializers.CarsSerializer