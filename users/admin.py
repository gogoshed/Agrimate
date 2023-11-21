from django.contrib import admin
from .models import Crop, Livestock, UserProfile, equipment, Expense, MarketPrice, CropPlanting, Field



@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'planting_season', 'harvest_season')
    list_filter = ('planting_season', 'harvest_season')
    search_fields = ('name',)

# Register your models here.
# admin.site.register(Crop)

@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'health_status', 'gender', 'date_of_birth', 'vaccination_records')
    list_filter = ('health_status', 'gender', 'species')
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'address', 'role')
    list_filter = ('user', 'role')
    search_fields = ('user',)

@admin.register(equipment)
class equipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'purchase_date', 'Last_maintenance', 'Availability')
    list_filter = ('type', 'description', 'Availability')
    search_fields = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'amount', 'description')
    list_filter = ('category', 'amount')
    search_fields = ('date',)

@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_display = ('crop', 'date', 'price_per_unit', 'market_name')
    list_filter = ('price_per_unit', 'market_name')
    search_fields = ('crop',)

@admin.register(CropPlanting)
class CropPlantingAdmin(admin.ModelAdmin):
    list_display = ('crop', 'field', 'planting_date', 'quantity', 'notes')
    list_filter = ('planting_date', 'quantity', 'field')
    search_fields = ('crop',)

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'size_in_acres', 'soil_type', 'irrigation_method', 'location_coordinates')
    list_filter = ('size_in_acres', 'soil_type')
    search_fields = ('name',)