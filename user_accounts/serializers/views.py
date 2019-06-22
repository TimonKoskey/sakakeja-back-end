from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from django.core.mail import send_mail
from rest_framework.parsers import MultiPartParser
import json

from rest_framework.generics import (
	CreateAPIView,
	RetrieveUpdateAPIView,
	ListAPIView,
	RetrieveAPIView,
	)

from .serializers import (
	CreateNewPropertySerializer,
	LocationSerializer,
	UploaderDetailsSerializer,
	UserCreateSerializer
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

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
user=get_user_model()

class SignInUsers(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        mymeta = request.META.get('USER')
        serializer = ObtainJSONWebToken.get_serializer(self,data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            uploader_class_obj=uploader_details.objects.get(user=user)
            uploader_details_serializer=UploaderDetailsSerializer(uploader_class_obj)

            response_data = {
				'user':uploader_details_serializer.data,
				'token':jwt_response_payload_handler(token, user, request),
			}
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True,
                                    )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpUsers(ObtainJSONWebToken):
	def post(self,request,*args,**kwargs):
		print(request.data)
		request_data=request.data
		user_data={
			'username':request_data['username'],
			'first_name':request_data['first_name'],
			'last_name':request_data['last_name'],
			'email':request_data['email'],
			'password':request_data['password'],
		}

		user_serializer=UserCreateSerializer(data=user_data)
		if user_serializer.is_valid():
			user_validated_data=user_serializer.create(user_serializer.validated_data)
			user_login_cred={
				'username':user_validated_data['username'],
				'password':user_validated_data['password']
			}
			login_serializer=ObtainJSONWebToken.get_serializer(self,data=user_login_cred)

			if login_serializer.is_valid():
				user = login_serializer.object.get('user')
				uploader_class_obj=uploader_details(user=user)
				uploader_class_obj.save()
				uploader_details_serializer=UploaderDetailsSerializer(uploader_class_obj)

				token = login_serializer.object.get('token')
				response_data = {
					'user':uploader_details_serializer.data,
					'token':jwt_response_payload_handler(token, user, request),
				}
				response = Response(response_data)

				return response

			return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateNewPropertyAPIView (APIView):
    parser_class = (MultiPartParser)

    def post(self, request, *args, **kwargs):
        post_data=request.data
        uploader = post_data['uploader']
        uploader = json.loads(uploader)
        image_count=int(post_data['image_count'])

        # for image_c in range(image_count):
        #     property_obj=property_class.objects.get(property_type='Apartment')
        #     image = post_data[('image'+str(image_c))]
        #     picture_obj = property_picture(property=property_obj,picture=image)
        #     picture_obj.save()

        property_details = post_data['property_details']
        property_details = json.loads(property_details)

        property_data_to_save = {
            'title': property_details['title'],
            'amount_to_be_paid': property_details['amount_to_be_paid'],
            'property_type': property_details['property_type'],
            'rent_or_sale': property_details['rent_or_sale'],
            'property_name': property_details['property_name'],
            'number_of_bedrooms': property_details['number_of_bedrooms'],
            'number_of_bathrooms': property_details['number_of_bathrooms'],
            'description': property_details['description']
        }

        location_data_to_save= {
            'county': property_details['location']['county'],
            'city_or_town': property_details['location']['city_or_town'],
            'estate_or_area_name': property_details['location']['estate_or_area_name']
        }

        property_serializer=CreateNewPropertySerializer(data=property_data_to_save)

        if property_serializer.is_valid():
            property_obj = property_serializer.create(property_serializer.validated_data)
            location_serializer = LocationSerializer (data=location_data_to_save)
            if location_serializer.is_valid():
                location_obj=location_serializer.create(location_serializer.validated_data)
                property_obj.location=location_obj
                user_obj = uploader_details.objects.get(id=uploader['id'])
                property_obj.uploader=user_obj
                property_obj.save()
                for image_c in range(image_count):
                    image = post_data[('image'+str(image_c))]
                    if image:
                        picture_obj = property_picture(property=property_obj,picture=image)
                        picture_obj.save()
            return Response(CreateNewPropertySerializer(property_obj).data, status=status.HTTP_201_CREATED)
        return Response(CreateNewPropertySerializer(property_obj).errors, status=status.HTTP_400_BAD_REQUEST)
