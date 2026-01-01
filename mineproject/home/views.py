from django.shortcuts import render
from django.http import HttpResponse
from .models import Shishir


peoples=[{"name":"shreeram","age":17,"city":"dhaka"},
    {"name":"shishir","age":12,"city":"dhaka"},
    {"name":"ram","age":25,"city":"kathmandu"},
    {"name":"sita","age":18,"city":"pokhara"},
    {"name":"gita","age":20,"city":"biratnagar"},
]

# Create your views here.
def home(request):
    return render(request, "htmls/index.html",context={"peoples":peoples,"shishir":"developer"})

def about(request):
    return render(request, "htmls/about.html")

def contact(request):
    return render(request, "htmls/contact.html")
# home/views.py


def create_shishir(request):
    if request.method == "POST":
        # Get data from form
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        # Create object in DB
        Shishir.objects.create(
            name=name,
            age=int(age),
            city=city,
            phone=int(phone),
            email=email
        )

        return HttpResponse(f"Shishir {name} created successfully!")

    # For GET requests, show a simple form
    return render(request, "htmls/form.html")
