from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "firstapp/index.html")


def contact(request):
    if request.method == "POST":
        contacts = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contacts.name = name
        contacts.email = email
        contacts.message = message
        contacts.save()
        return HttpResponse("<h1>Thanks for contacting Us <h1>")

    return render(request, "firstapp/index.html")

