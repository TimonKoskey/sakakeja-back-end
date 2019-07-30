from django.contrib import admin
from user_accounts.models import (
    location,
    uploader_details,
    )

admin.site.register(location)
admin.site.register(uploader_details)

# Register your models here.
