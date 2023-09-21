from django.shortcuts import render

from .models import PackageTheme, PackageType, Destination


def home(request):
    template_name = "trips/home.html"

    package_themes = PackageTheme.objects.all()
    context = {"package_themes": package_themes}

    return render(request, template_name, context)

def destinations(request, pk, slug):
    template_name = "trips/destinations.html"

    destinations = Destination.objects.filter(package_theme__id=pk)
    context = {"destinations": destinations}

    return render(request, template_name, context)