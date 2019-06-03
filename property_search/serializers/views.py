from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
	CreateAPIView,
	RetrieveAPIView,
	ListAPIView,
	RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
	)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	IsAdminUser,
	)

from property_search.models import (
    location,
    uploader_details,
    property_class,
    property_picture
)

from .serializers import (
    PropertyListSerializer,
    LocationSerializer,
    PropertyDetailSerializer
)

import json

class PrimarySearchResultsAPIView (ListAPIView):
    serializer_class = PropertyListSerializer
	# property_type, number_of_bedrooms, size, location, max_amount

    def get_queryset(self, *args, **kwargs):
        # property_list_queryset = []
        property_list = property_class.objects.all()
        request_data = self.request.GET
        Location_data = request_data['location']
        rent_or_sale = request_data['rent_or_sale']
        property_type = request_data['property_type']
        number_of_bedrooms = request_data['number_of_bedrooms']
        max_amount = request_data['max_amount']

        if property_type != 'null' and property_type != None and property_type != '':
            property_list.filter(property_type=property_type)

        if number_of_bedrooms != 'null' and number_of_bedrooms != None and number_of_bedrooms != '':
            property_list.filter(number_of_bedrooms=number_of_bedrooms)

        if Location_data != 'null' and Location_data != None and Location_data!= '':
            location_list = location.objects.all()
            Location_data = json.loads(Location_data)
            city_or_town = (Location_data['city_or_town'])
            estate_or_area_name = (Location_data['estate_or_area_name'])

            if ((city_or_town != 'null' and city_or_town != None and city_or_town != '') and (estate_or_area_name == 'null' or estate_or_area_name == None or estate_or_area_name == '')):
                location_list = location_list.filter(city_or_town__icontains=city_or_town)

            if ((city_or_town == 'null' or city_or_town == None or city_or_town == '') and (estate_or_area_name != 'null' and estate_or_area_name != None and estate_or_area_name != '')):
                location_list = location_list.filter(estate_or_area_name__icontains=estate_or_area_name)

            if ((city_or_town != 'null' and city_or_town != None and city_or_town != '') and (estate_or_area_name != 'null' and estate_or_area_name != None and estate_or_area_name != '')):
                location_list = location_list.filter(city_or_town__icontains=city_or_town)
                loc_list_1 = list(location_list)
                if location_list:
                    location_list = location_list.filter(estate_or_area_name__icontains=estate_or_area_name)
                    loc_list_2 = list(location_list)
                    location_list = loc_list_2.extend(loc_list_1)


            if location_list:
                property_list_queryset = []
                for prop_obj in property_list:
                    for loc_obj in location_list:
                        if prop_obj.location == loc_obj:
                            property_list_queryset.append(prop_obj)

                property_list = property_list_queryset

        if max_amount != 'null' and max_amount != None and max_amount != '':
            new_property_list = []
            for obj in property_list:
                if int(obj.amount_to_be_paid) <= int(max_amount):
                    new_property_list.append(obj)
            property_list = new_property_list

        return property_list

class LatestPropertyListAPIView (ListAPIView):
    serializer_class = PropertyListSerializer

    def get_queryset(self, *args, **kwargs):
        property_list = property_class.objects.all()
        property_list_count = property_list.count()

        if property_list_count <= 6:
            return property_list
        else:
            return property_list[(property_list_count - 6):]

class LocationListAPIView (ListAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self, *args, **kwargs):
        location_list = location.objects.all()
        return location_list

class PropertyDetailsAPIView(RetrieveAPIView):
    queryset = property_class
    serializer_class = PropertyDetailSerializer
