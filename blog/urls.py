"""importing the 'path" and 'views' functions from the "blog/views.py" application
urlpatterns  - URL template
for Django URL handlers, 'http://127.0.0.1:8000/' is not part of the URL. This template will tell Django
that views.post_list is the correct direction to request the website at 'http://127.0.0.1:8000/'.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]