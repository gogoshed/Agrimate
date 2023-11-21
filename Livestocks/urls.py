from django.urls import path
from . import views


urlpatterns = [   
    path('', views.livestocks, name='livestocks'),
    # path('Lhome/', views.Lhome, name='Lhome'), this didnt allow some data to show
    path('livestock/create/', views.create_livestock, name='create-livestock'),
    path('livestock/', views.livestock_Dashboard, name='livestock-Dashboard'),
    path('livestock/update/<str:pk>/', views.update_livestock, name='update-livestock'),
    path('livestock/delete/<int:livestock_id>/', views.delete_livestock, name='delete-livestock'),
    path('livestock/chart/', views.livestock_chart_data, name='livestock-chart-data'),

]