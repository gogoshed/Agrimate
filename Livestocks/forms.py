from django import forms
from .models import Livestock, BreedingEvent, PregnancyEvent, CalvingEvent

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ('name', 'species', 'tag_number', 'breed', 'health_status', 'gender', 'date_of_birth', 'vaccination_records')

class BreedingEventForm(forms.ModelForm):
    class Meta:
        model = BreedingEvent
        fields = '__all__'

class PregnancyEventForm(forms.ModelForm):
    class Meta:
        model = PregnancyEvent
        fields = '__all__'

class CalvingEventForm(forms.ModelForm):
    class Meta:
        model = CalvingEvent
        fields = '__all__'