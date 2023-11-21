from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView
from .models import Livestock, BreedingEvent, PregnancyEvent, CalvingEvent
from .forms import LivestockForm, BreedingEventForm, CalvingEventForm, PregnancyEventForm
import json
from django.http import JsonResponse
from collections import Counter


def livestock_chart_data(request):
    livestock_data = Livestock.objects.all()
    
    gender_counts = Counter([livestock.gender for livestock in livestock_data])
 
    # Extract labels (genders) and data values (counts) from the Counter object
    labels = list(gender_counts.keys())
    data = list(gender_counts.values())

    # Convert data to a dictionary
    chart_data = {
        'labels': labels,
        'data': data,
    }

    # Convert data to a format suitable for Chart.js (e.g., JSON)
    # chart_data = {
    #     'labels': [livestock.name for livestock in livestock_data],
    #     'data': [livestock.gender for livestock in livestock_data],  # Replace with the appropriate data you want to display
    # }
    
    return JsonResponse(chart_data)

def livestocks(request):
    return render(request, 'Livestocks\livestock_Dashboard.html')

def Lhome(request):
    return render(request, 'Livestocks\livestock_Dashboard.html')

# this method defines the post request to create crop from a form
def create_livestock(request):
    form = LivestockForm()
    if request.method == 'POST':
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('livestock-list')  # Redirect to a list view
            return redirect('Dashboard')  # Redirect to a list view
    
    return render(request, 'Livestocks/create_livestock.html', {'form': form})


def livestock_Dashboard(request):
    livestock = Livestock.objects.all()
    return render(request, 'Livestocks/livestock_Dashboard.html', {'livestock': livestock})

def update_livestock(request, pk):
    livestock = get_object_or_404(Livestock, pk=pk)
    if request.method == 'POST':
        form = LivestockForm(request.POST, instance=livestock)
        if form.is_valid():
            form.save()
            return redirect('livestock-list')  # Redirect to a success page or another URL

    else:
        # If it's a GET request, display the form pre-populated with the livestock data
        form = LivestockForm(instance=livestock)

    return render(request, 'Livestocks/update_livestock.html', {'form': form, 'livestock': livestock})


#     form = LivestockForm()
#     context = {}
#     return render(request, 'Livestocks/create_livestock.html', context)

def delete_livestock(Livestock, livestock_id):
    Livestock = get_object_or_404(Livestock, pk=livestock_id)
    
    if request.method == 'POST':
        Livestock.delete()
        return redirect('livestock-list')  # Redirect to a list view
    
    return render(request, 'Livestock/delete_livestock.html', {'Livestock': Livestock})

#The area of code is for breeding 
def breeding_event_list(request):
    breeding_events = BreedingEvent.objects.all()
    return render(request, 'breeding_event_list.html', {'breeding_events': breeding_events})

# View for creating a new breeding event
def breeding_event_create(request):
    if request.method == 'POST':
        form = BreedingEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breeding-event-list')  # Replace with the actual URL name
    else:
        form = BreedingEventForm()
    return render(request, 'breeding_event_form.html', {'form': form})