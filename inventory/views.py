from django.shortcuts import render

def inventory_home(request):
    return render(request, "home.html")   # or create a template later
