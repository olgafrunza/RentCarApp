from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'plate_number',
            'make',
            'model',
            'gear',
            'year',
            'rent_per_day',
        )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'car',
            'start_date',
            'end_date',
            'customer',
        )
