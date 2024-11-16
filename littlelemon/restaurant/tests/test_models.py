from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_menu_str_representation(self):
        # Create a new instance of the Menu model
        menu_item = Menu.objects.create(title="Pasta", price=12.99, inventory=20)

        # Expected string representation
        expected_value = "Pasta : 12.99"

        # Compare the string representation of the instance with the expected value
        self.assertEqual(str(menu_item), expected_value)
