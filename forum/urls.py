# forum/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('forum/', views.forum_index, name='forum_index'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('create_thread/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/create_post/', views.create_post, name='create_post'),
]
