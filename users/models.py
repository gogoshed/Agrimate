from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields for the user profile

# views.py
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    # Your profile view code here


# Create your models here.
# farm_management/models.py
class Livestock(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    health_status = models.CharField(max_length=100)
    vaccination_records = models.TextField()
    sex = models.CharField(max_length=10)
    sire = models.CharField(max_length=100)
    dam = models.CharField(max_length=100)
class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    planting_season = models.CharField(max_length=100)
    harvest_season = models.CharField(max_length=100)
    optimal_soil_type = models.CharField(max_length=100)
    optimal_sunlight = models.CharField(max_length=100)
    optimal_temperature = models.CharField(max_length=100)



# Define other models similarly...
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='Your Full Name')
    phone_number = models.CharField(max_length=20, default='Your Phone Number')
    address = models.CharField(max_length=200, default='Your Default Address')
    role = models.CharField(max_length=255, default='Define roles as needed')  # Define roles as needed

class equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    purchase_date = models.DateField(help_text="Enter the date of purchase")
    Last_maintenance = models.DateTimeField(help_text="Enter the date of purchase")
    Availability = models.CharField(max_length=20)

class Field(models.Model):
    name = models.CharField(max_length=100)
    size_in_acres = models.DecimalField(max_digits=5, decimal_places=2)
    soil_type = models.CharField(max_length=100)
    irrigation_method = models.CharField(max_length=100)
    location_coordinates = models.CharField(max_length=100)

class CropPlanting(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    planting_date = models.DateField()
    quantity = models.PositiveIntegerField()
    notes = models.TextField()

# Define other models similarly...

class MarketPrice(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    market_name = models.CharField(max_length=100)

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()