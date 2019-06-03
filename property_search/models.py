from django.db import models

# TYPE_OPTIONS = (
#     ('Apartments','Apartments'),
#     ('Houses','Houses'),
#     ('Hostels','Hostels'),
#     ('Offices-Bussiness units','Offices-Bussiness units'),
# )

class Location (models.Model):
    county = models.CharField (max_length = 50,null=True, blank = True)
    city_or_town = models.CharField (max_length = 50,null=True, blank = True)
    estate_or_area_name = models.CharField (max_length = 50,null=True, blank = True)

    def __str__(self):
        return "%s - %s" %(self.estate_or_area_name,self.city_or_town)

class DetailsOfUploader (models.Model):
    first_name = models.CharField (max_length = 50,null=True, blank = True)
    last_name = models.CharField (max_length = 50,null=True, blank = True)
    phone_number = models.IntegerField (null=True, blank = True)
    email = models.EmailField(null=True, blank = True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null = True, blank = True)
    company_name = models.CharField (max_length = 50,null=True, blank = True)

class Property (models.Model):
    title = models.CharField (max_length = 100,null=True)
    property_type = models.CharField (max_length = 50,null=True)
    rent_or_sale = models.CharField (max_length = 50,null=True, blank = True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null = True, blank = True)
    number_of_bedrooms = models.IntegerField (null=True, blank = True)
    number_of_bathrooms = models.IntegerField (null=True, blank = True)
    description = models.CharField (max_length = 1000,null=True, blank = True)
    amount_to_be_paid = models.IntegerField (null=True, blank = True)
    uploader = models.ForeignKey(DetailsOfUploader, on_delete=models.SET_NULL,null = True, blank = True)
    date_of_upload = models.DateTimeField(auto_now_add=True)

# class Land(models.Model):
#     property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
#     size_in_acres = models.CharField (max_length = 100,null=True, blank = True)

# class ResidentialBuildings(models.Model):
#     property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
#     number_of_bedrooms = models.IntegerField (null=True, blank = True)
#     number_of_bathrooms = models.IntegerField (null=True, blank = True)

# class OfficesBusinessAndStoreSpace(models.Model):
#     property_class = models.OneToOneField(Property, on_delete = models.CASCADE,null = True, blank = True)
#     size_in_square_feet = models.CharField (max_length = 100,null=True, blank = True)

class PropertyPicture (models.Model):
    property = models.ForeignKey(Property, on_delete = models.CASCADE,null = True, blank = True)
    picture = models.FileField(null = True, blank = True)

location = Location
uploader_details = DetailsOfUploader
property_class = Property
property_picture = PropertyPicture
