from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'  # Customize the template name

# Create your views here.
# views.py
# def users(request):
#     pass

def login_user(request):
    return render(request, 'users/registration/login.html', {})
    #return render(request, 'users/registration/login.html', context)




# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in after registration
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/registration/register.html', {'form': form})


@login_required
def dashboard(request):
    # Your dashboard view code here
    pass



# Create groups for different user roles
# @group_required
#     farmer_group, created = Group.objects.get_or_create(name='Farmer')
#     expert_group, created = Group.objects.get_or_create(name='Expert')

# Assign users to groups
    User.groups.add(farmer_group)






@login_required
def dashboard(request):
    # Retrieve user-specific data or perform any necessary queries here
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Assuming you have a UserProfile model
    # You can add more data retrieval here

    context = {
        'user': user,
        'user_profile': user_profile,
        # Add more context data as needed
    }

    return render(request, 'users/registration/dashboard.html', context)





def home(request):
    return render(request, 'users/home.html')

def user_login(request):
    if request.method == 'POST':
        # Handle user login authentication
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a dashboard or other authenticated view
            return redirect('dashboard')
        else:
            # Handle authentication failure (e.g., show an error message)
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'users/registration/login.html')
