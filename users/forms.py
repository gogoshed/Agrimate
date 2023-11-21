from django import forms
from .models import Livestock, Crop, UserProfile, equipment, Field, CropPlanting, MarketPrice, Expense

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ('name', 'description', 'planting_season', 'harvest_season', 'optimal_soil_type', 'optimal_sunlight', 'optimal_temperature')

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ('name', 'species', 'breed', 'health_status', 'gender', 'date_of_birth', 'vaccination_records')

class UserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'full_name', 'phone_number', 'address', 'role')

class equipment(forms.ModelForm):
    class Meta:
        model = equipment
        fields = ('name', 'type', 'description', 'purchase_date', 'Last_maintenance', 'Availability')

class Field(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'size_in_acres', 'soil_type', 'irrigation_method', 'location_coordinates')

class CropPlanting(forms.ModelForm):
    class Meta:
        model = CropPlanting
        fields = ('crop', 'field', 'planting_date', 'quantity', 'notes')

class MarketPrice(forms.ModelForm):
    class Meta:
        model = MarketPrice
        fields = ('crop', 'date', 'price_per_unit', 'market_name')


class Expense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'category', 'amount', 'description')
