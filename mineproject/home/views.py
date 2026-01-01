from django.shortcuts import render
from django.http import HttpResponse



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