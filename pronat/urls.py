from django.urls import path

from . import views

app_name = 'pronat'

urlpatterns = [
    path('', views.properties_all, name="home_page"),
    path('property/<slug:slug>', views.property_detail, name = "property_detail"),
]