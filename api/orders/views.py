from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TransportOrder
from .serializers import TransportOrderSerializer

class TransportOrderListCreateView(generics.ListCreateAPIView):
    queryset = TransportOrder.objects.all().order_by('-date')
    serializer_class = TransportOrderSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['customer_name', 'date']
    ordering_fields = ['customer_name', 'date']
    search_fields = ['customer_name', 'order_number'] 
