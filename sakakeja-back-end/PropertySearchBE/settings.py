import os

if 'DJANGO_SETTINGS' in os.environ:
    if os.environ['DJANGO_SETTINGS'] == "production":
        print ("PROD SERVER")
        from .settings_prodmod import *
else:
    print ("DEV SERVER")
    from .settings_devmod import *
