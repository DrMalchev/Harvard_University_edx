from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight")

]

# path("<int:flight_id>", views.flight, name="flight") gives argument flight_id which is int to views.py