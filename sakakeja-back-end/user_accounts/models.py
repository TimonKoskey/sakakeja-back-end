from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()

class Location (models.Model):
    county = models.CharField (max_length = 50,null=True, blank = True)
    city_or_town = models.CharField (max_length = 50,null=True, blank = True)
    estate_or_area_name = models.CharField (max_length = 50,null=True, blank = True)

    def __str__(self):
        return "%s - %s" %(self.estate_or_area_name,self.city_or_town)

class DetailsOfUploader (models.Model):
	user = models.OneToOneField(user,on_delete=models.CASCADE,null = True, blank = True)
	main_phone_number = models.IntegerField (null=True, blank = True)
	alternative_phone_number = models.IntegerField (null=True, blank = True)
	company_name = models.CharField (max_length = 50,null=True, blank = True)
	office_location = models.ForeignKey(Location, on_delete=models.SET_NULL,null = True, blank = True)
	office_address = models.CharField (max_length = 50,null=True, blank = True)

uploader_details = DetailsOfUploader
location = Location
