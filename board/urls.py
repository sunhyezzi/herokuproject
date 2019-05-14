from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('post/', views.post,name='post'), 
    path('<int:board_id>/', views.detail, name='detail'),
    path('show/', views.show, name='show'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('info/', views.info, name='info'),
]