from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns
    #path('register/', views.register, name='register'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),




]






# # myapp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='login'),
#     # Add more URL patterns as needed
# ]
