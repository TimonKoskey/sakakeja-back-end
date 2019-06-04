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

		def create (self, validated_data):
			county=validated_data['county']
			city_or_town=validated_data['city_or_town']
			estate_or_area_name=validated_data['estate_or_area_name']

			location_obj=location(county=county, city_or_town=city_or_town, estate_or_area_name=estate_or_area_name)
			location_obj.save()
			return location_obj

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
			'property_name',
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
			'property_name',
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

class CreateNewPropertySerializer(ModelSerializer):

	class Meta:
		model=property_class
		fields=[
			'title',
			'amount_to_be_paid',
			'property_type',
			'rent_or_sale',
			'property_name',
		    'number_of_bedrooms',
		    'number_of_bathrooms',
		    'description',
		]

	def create (self, validated_data):
		title=validated_data['title']
		amount_to_be_paid=validated_data['amount_to_be_paid']
		property_type=validated_data['property_type']
		rent_or_sale=validated_data['rent_or_sale']
		property_name=validated_data['property_name']
		number_of_bedrooms=validated_data['number_of_bedrooms']
		number_of_bathrooms=validated_data['number_of_bathrooms']
		description=validated_data['description']

		property_obj = property_class(title=title, amount_to_be_paid=amount_to_be_paid, property_type=property_type,
			rent_or_sale=rent_or_sale, property_name=property_name, number_of_bedrooms=number_of_bedrooms,
			number_of_bathrooms=number_of_bathrooms,description=description)

		property_obj.save()

		return property_obj