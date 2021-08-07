from django.shortcuts import render, redirect, HttpResponse
from .models import dojo, ninja

def index(request):
    context = {
    "all_the_dojos": dojo.objects.all(),
    "all_the_ninjas": ninja.objects.all(),
    }
    return render(request, "index.html", context)

def new_dojo(request):
    if request.method == "POST":
        dojo.objects.create(name = request.POST["dojo_name"], city = request.POST["city"], state = request.POST["state"])
    return redirect('/')

def new_ninja(request):
    if request.method == "POST":
        ninja.objects.create(dojo = dojo.objects.get(id=request.POST["dojo"]), first_name = request.POST["ninja_first_name"], last_name = request.POST["ninja_last_name"])
    return redirect('/')