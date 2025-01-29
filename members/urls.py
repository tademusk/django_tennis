from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name = "members"),
    path('', views.first, name = "first"),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),  
]

