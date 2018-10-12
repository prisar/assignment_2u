from rest_framework import serializers

from .models import Screen, Seat

class ScreenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Screen
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    seats = ScreenSerializer(read_only=True, many=True)
    
    class Meta:
        model = Seat
        fields = '__all__'