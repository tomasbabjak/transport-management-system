from django.db import models

class TransportOrder(models.Model):
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

class Waypoint(models.Model):
    PICKUP = 'Pickup'
    DELIVERY = 'Delivery'
    TYPE_CHOICES = [(PICKUP, 'Pickup'), (DELIVERY, 'Delivery')]

    order = models.ForeignKey(TransportOrder, related_name='waypoints', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    waypoint_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
