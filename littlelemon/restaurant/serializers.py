from rest_framework import serializers
from .models import Menu
from .models import Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Link the serializer to the Menu model
        fields = '__all__'  # Include all fields from the Menu model




class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the Booking model
        fields = '__all__'  # Include all fields in the model
