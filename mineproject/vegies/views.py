from django.shortcuts import render

# Create your views here.

def first_look(request):
    return render(request, 'frontend/index.html')
