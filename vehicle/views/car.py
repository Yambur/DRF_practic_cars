from rest_framework import viewsets

from vehicle.models import Car
from vehicle.serializers.car import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()