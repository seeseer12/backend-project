from django.contrib import admin
from django.urls import path
from home.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("create/", views.create_shishir, name="create_shishir"),
]