# from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Shishir

@admin.register(Shishir)
class ShishirAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone', 'city')
