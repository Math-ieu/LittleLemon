# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Handles POST and GET requests for the list of Menu items
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()  # Fetch all menu items from the database
    serializer_class = MenuSerializer  # Use the MenuSerializer for data serialization

# Handles GET, PUT, and DELETE requests for a single Menu item
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Fetch all menu items from the database
    serializer_class = MenuSerializer  # Use the MenuSerializer for data serialization



class BookingViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing Booking instances.
    """
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use BookingSerializer for serialization
    permission_classes = [permissions.IsAuthenticated]
