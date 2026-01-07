from vegies.views import *
from django.urls import path
from . import views
urlpatterns = [
    path("", views.first_look, name="first_look"),
]