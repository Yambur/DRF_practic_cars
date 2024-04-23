from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views.car import CarViewSet

app_name = VehicleConfig

router = DefaultRouter()
router.register('car', CarViewSet, basename='cars')

urlpatterns = [

] + router.urls
