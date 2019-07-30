from django.db import models
from user_accounts.models import (
    location,
    uploader_details,
    )

class Property (models.Model):
    property_name = models.CharField (max_length = 50,null=True, blank = True)
    title = models.CharField (max_length = 100,null=True, blank = True)
    property_type = models.CharField (max_length = 50,null=True, blank = True)
    rent_or_sale = models.CharField (max_length = 50,null=True, blank = True)
    location = models.ForeignKey(location, on_delete=models.SET_NULL,null = True, blank = True)
    number_of_bedrooms = models.IntegerField (null=True, blank = True)
    number_of_bathrooms = models.IntegerField (null=True, blank = True)
    description = models.CharField (max_length = 1000,null=True, blank = True)
    amount_to_be_paid = models.IntegerField (null=True, blank = True)
    uploader = models.ForeignKey(uploader_details , on_delete=models.SET_NULL,null = True, blank = True)
    date_of_upload = models.DateTimeField(auto_now_add=True)

class Land(models.Model):
    property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
    size_in_acres = models.CharField (max_length = 100,null=True, blank = True)

class ResidentialBuildings(models.Model):
    property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
    number_of_bedrooms = models.IntegerField (null=True, blank = True)
    number_of_bathrooms = models.IntegerField (null=True, blank = True)

class OfficesBusinessAndStoreSpace(models.Model):
    property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
    size_in_square_feet = models.CharField (max_length = 100,null=True, blank = True)

class PropertyPicture (models.Model):
    property = models.ForeignKey(Property, on_delete = models.CASCADE,null = True, blank = True)
    picture = models.FileField(null = True, blank = True)

property_class = Property
land = Land
residential_buildings = ResidentialBuildings
offices_bussinesses_and_store = OfficesBusinessAndStoreSpace
property_picture = PropertyPicture
