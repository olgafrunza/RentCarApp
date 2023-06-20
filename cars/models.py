from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    plate_number = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    GEAR = (
        ('a', 'Automatic'),
        ('m', 'Manuel')
    )
    gear = models.CharField(max_length=1, choices=GEAR)
    rent_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    out_of_service = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.plate_number} - {self.model} - {self.year}'


class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start_date} - {self.end_date}'
