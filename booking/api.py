from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ScreenSerializer, SeatSerializer
from .models import Screen, Seat

class ScreenViewSet(ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    permission_classes = (permissions.IsAuthenticated,)

class SeatViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (permissions.IsAuthenticated,)