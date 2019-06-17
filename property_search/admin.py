from django.contrib import admin
from .models import (
    property_class,
    property_picture
)

class PhotosInline (admin.TabularInline):
    model = property_picture

class PropertyAdmin (admin.ModelAdmin):

    inlines = [ PhotosInline ]

    def get_formsets_with_inlines(self,request,obj=None):
        for inline in self.get_inline_instances(request,obj):
            yield inline.get_formset(request,obj),inline

admin.site.register(property_class, PropertyAdmin)

# Register your models here.
