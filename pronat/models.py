from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
#g
ACTION_OPTION = (
        ("Sale", "Shitje"),
        ("Rent", "Qera")
    )

PROPERTY_TYPE = (
        ("Apartament", "Apartament"),
        ("Vila", "Vila"),
        ("Store", "Dyqan"),
        ("Land", "Truall"),
        ("Garage", "Garazhd"),
    )

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class City(models.Model):
    name = models.CharField(verbose_name="Emri", help_text="E nevojshme", max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Qyteti"
        verbose_name_plural = "Qytetet"

    def __str__(self):
        return self.name


class District(models.Model):
    city_id = models.ForeignKey(City, on_delete=CASCADE)
    name = models.CharField(verbose_name="Emri", help_text="E nevojshme", max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonat"

    def __str__(self):
        return self.name


class Property(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_creator')
    title = models.CharField(verbose_name="Titulli", help_text="Vendos titullin e njoftimit", max_length=500)
    description = models.CharField(verbose_name="Pershkrimi", help_text="Vendos pershkrimin",max_length=1000)
    price = models.IntegerField()
    area = models.ImageField()
    views = models.IntegerField(default=0)
    documents = models.CharField(verbose_name="Dokumentacioni", help_text="Dokumentat", max_length=255)
    status = models.BooleanField(default=True)
    activity = models.CharField(max_length=20, choices=ACTION_OPTION)
    property_type = models.CharField(max_length=20,choices=PROPERTY_TYPE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = "Prona"
        verbose_name_plural = "Pronat"

    def __str__(self):
        return self.name

    
class Address(models.Model):
    district_id = models.ForeignKey(District, on_delete=CASCADE)
    address_line = models.CharField(verbose_name="Adresa", help_text="E nevojeshme")

    class Meta:
        verbose_name = "Adresa"

    def __str__(self):
        return self.name


class Apartment(models.Model):
    property_id = models.ForeignKey(Property, on_delete=CASCADE, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    floor = models.IntegerField(default=0)
    room_num = models.IntegerField(default=0)
    bath_num = models.IntegerField(default=0)
    balcony_num = models.IntegerField(default=0)


class Villa(models.Model):
    property_id = models.ForeignKey(Property, on_delete=CASCADE, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    floors = models.IntegerField(default=1)
    room_num = models.IntegerField(default=1)
    bath_num = models.IntegerField(default=1)
    balcony_num = models.IntegerField(default=0)


class Store(models.Model):
    property_id = models.ForeignKey(Property, on_delete=CASCADE, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    floor = models.IntegerField(default=0)
    bath_num = models.IntegerField(default=1)


class Land(models.Model):
    property_id = models.ForeignKey(Property, on_delete=CASCADE, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

class Garage(models.Model):
    property_id = models.ForeignKey(Property, on_delete=CASCADE, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    floor = models.IntegerField()


class PropertyImage(models.Model):


    product = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_image")
    image = models.ImageField(
        verbose_name= "image",
        help_text="Upload a property image",
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name="Alturnative text",
        help_text="Please add alturnative text",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"