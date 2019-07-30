from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from user_accounts.models import (
	location,
    uploader_details,
    )

from property_search.models import (
    property_class,
    property_picture
)

from django.contrib.auth import get_user_model

user=get_user_model()


class UserDetailsSerializer(ModelSerializer):

	class Meta:
		model = user
		fields=[
			"username",
			"first_name",
			"last_name",
			"email"
		]

class UserCreateSerializer(ModelSerializer):

	class Meta:
		model = user
		fields=[
			"username",
			"first_name",
			"last_name",
			"email",
			"password"
		]
		extra_kwargs={"password":
							{"write_only":True}
							}

	def create(self, validated_data):
		username=validated_data['username']
		first_name=validated_data['first_name']
		last_name=validated_data['last_name']
		email=validated_data['email']
		password=validated_data['password']

		user_obj = user(
			username=username,
			first_name=first_name,
			last_name=last_name,
			email=email
		)

		user_obj.set_password(password)
		user_obj.save()

		return validated_data

class UploaderDetailsSerializer(ModelSerializer):
	user = SerializerMethodField()

	class Meta:
		model = uploader_details
		fields= [
		'id',
		'user',
		'main_phone_number',
		'alternative_phone_number',
		'company_name',
		'office_location',
		'office_address'
		]

	def get_user(self, obj):
		user_obj = obj.user
		user = UserDetailsSerializer(user_obj).data
		return user

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
