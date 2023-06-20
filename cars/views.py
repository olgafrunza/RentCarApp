from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from .serializers import (
    CarSerializer,
    ReservationSerializer,
)
from .models import (
    Car,
    Reservation,
)
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the cars
        to the admins, and only available cars to the 
        authenticated user.
        """
        user = self.request.user
        if user.is_staff:
            queryset = super().get_queryset()
        queryset = super().get_queryset().filter(out_of_service=False)

        start = self.request.query_params.get('start')
        ends = self.request.query_params.get('end')

        if start and ends and start < ends:

            condition_1 = Q(start_date__gte=ends)
            condition_2 = Q(end_date__lte=start)

            # Django values_list() is an optimization to grab specific data from the database 
            # instead of building and loading the entire model instance.
            available1 = Reservation.objects.filter(condition_1).values_list('car_id', flat=True)
            # When grabbing a single value from the db, you can pass `flat=True` 
            # which will just give you back single value, instead of tuples
            
            available = Reservation.objects.filter(condition_1 & condition_2).values_list('car_id', flat=True)

            queryset = queryset.filter(id__in=available)

        return queryset


class ReservationListCreate(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


class ReservationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

