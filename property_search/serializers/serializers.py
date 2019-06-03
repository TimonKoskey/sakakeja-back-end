from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from property_search.models import (
    location,
    uploader_details,
    property_class,
    property_picture
)

class LocationSerializer (ModelSerializer):

	class Meta:
		model = location
		fields = '__all__'

class PropertyListSerializer(ModelSerializer):
	location = SerializerMethodField()
	pictures = SerializerMethodField()

	class Meta:
		model = property_class
		fields = [
			'id',
			'title',
			'location',
			'rent_or_sale',
			'amount_to_be_paid',
			'date_of_upload',
			'pictures'
		]
	def get_location(self,obj):
		location = LocationSerializer(obj.location).data
		return location

	def get_pictures(self,obj):
		pictures_objs = property_picture.objects.filter(property=obj)
		pictures = PropertyPictureSerializer(pictures_objs, many=True).data
		return pictures

class PropertyPictureSerializer (ModelSerializer):

	class Meta:
		model = property_picture
		fields = [
			'picture'
		]

class PropertyDetailSerializer (ModelSerializer):
	location = SerializerMethodField()
	uploader = SerializerMethodField()
	pictures = SerializerMethodField()

	class Meta:
		model=property_class
		fields=[
			'id',
			'title',
			'location',
			'amount_to_be_paid',
			'date_of_upload',
			'pictures',
    		'property_type',
    		'rent_or_sale',
		    'number_of_bedrooms',
		    'number_of_bathrooms',
		    'description',
		    'uploader',
		]

	def get_location(self,obj):
		location = LocationSerializer(obj.location).data
		return location

	def get_pictures(self,obj):
		pictures_objs = property_picture.objects.filter(property=obj)
		pictures = PropertyPictureSerializer(pictures_objs, many=True).data
		return pictures

	def get_uploader(self,obj):
		uploader = UploaderDetailsSerializer(obj.uploader).data
		return uploader

class UploaderDetailsSerializer(ModelSerializer):

	class Meta:
		model = uploader_details
		fields= '__all__'
