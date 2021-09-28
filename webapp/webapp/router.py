from cardetailsapi.viewsets import CarsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car', CarsViewset)