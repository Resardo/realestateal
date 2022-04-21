from msilib.schema import Property
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Property

def properties_all(request):
    properties = Property.objects.prefetch_related("property_image").filter(is_active=True)
    return render(request, "home/index.html", {"properties" : properties})

