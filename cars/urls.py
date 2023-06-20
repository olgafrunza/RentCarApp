from django.urls import path
from rest_framework import routers
from .views import (
    CarViewSet,
    ReservationListCreate,
    ReservationDetail,
)


router = routers.DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = [
   path('reservation/', ReservationListCreate.as_view()), 
   path('reservation/<int:pk>/', ReservationDetail.as_view()),
]

urlpatterns += router.urls
