from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your models here.
class Livestock(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    tag_number = models.CharField(max_length=20, unique=True)
    health_status = models.CharField(max_length=100)
    vaccination_records = models.CharField(max_length=30)
    # sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    sire = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='offspring')
    # dam = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='calves')
    # Add more fields such as color, weight, and health status.
    @staticmethod
    def get_default_dam():
        # Assuming there is a Livestock instance representing an unknown or default dam
        try:
            return Livestock.objects.get(name="Unknown Dam")
        except Livestock.DoesNotExist:
            # Handle the case where "Unknown Dam" instance does not exist
            # You might want to create it or choose another default behavior
            return None

    def default_dam():
        return Livestock.get_default_dam()

    dam = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, default=default_dam, related_name='calves')



class BreedingEvent(models.Model):
    date = models.DateField()
    sire = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='sired_events')
    dam = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='dam_events')
    # Add more fields to track the breeding event.

class PregnancyEvent(models.Model):
    date = models.DateField()
    # dam = models.ForeignKey( on_delete=models.SET_NULL, Livestock, related_name='pregnancy_events')
    dam = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='pregnancy_events')

    ultrasound_results = models.TextField()
    # Add more fields to track the pregnancy.

class CalvingEvent(models.Model):
    date = models.DateField()
    dam = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='calving_events')
    offspring = models.ForeignKey(Livestock, on_delete=models.CASCADE, related_name='birth_event')
    # Add more fields for tracking calving, such as birth weight and health status.
