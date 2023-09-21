from django.urls import path

from . import views

app_name = "trips"
urlpatterns = [
    path("", views.home, name="home"),
    path("destinations/<int:pk>/<slug:slug>/", views.destinations, name="destinations"),
]
