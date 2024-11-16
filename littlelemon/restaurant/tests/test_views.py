from django.test import TestCase
from ..models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from ..serializers import MenuSerializer  # Assuming you have a MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title="Pizza", price=8.99, inventory=10)
        self.menu_item2 = Menu.objects.create(title="Burger", price=5.49, inventory=15)
        self.menu_item3 = Menu.objects.create(title="Salad", price=4.99, inventory=20)

        # Initialize API client
        self.client = APIClient()

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/api/menu/')  # Assuming your endpoint is /menu/

        # Serialize the data
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
