from django.db import models

# Booking table model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # ID column
    name = models.CharField(max_length=255)  # Name column
    no_of_guests = models.IntegerField()  # No_of_guests column
    booking_date = models.DateTimeField()  # BookingDate column

    def __str__(self):
        return f"Booking by {self.name} for {self.no_of_guests} guests on {self.booking_date}"

# Menu table model
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # ID column
    title = models.CharField(max_length=255)  # Title column
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price column
    inventory = models.IntegerField()  # Inventory column

    def __str__(self):
      return f'{self.title} : {str(self.price)}'