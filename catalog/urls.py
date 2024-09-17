from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path("home/", views.home, name='home'),
    path("contacts/", views.contacts, name='contacts'),
]