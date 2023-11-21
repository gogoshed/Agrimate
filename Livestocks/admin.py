from django.contrib import admin
from .models import Livestock
@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'tag_number',  'health_status', 'gender', 'date_of_birth', 'vaccination_records')
    list_filter = ('health_status', 'gender', 'species')
    search_fields = ('name',)
