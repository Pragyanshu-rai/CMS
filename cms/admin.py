from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Doctor)

admin.site.register(Contact)

admin.site.register(Booking)

admin.site.register(Details)

admin.site.register(History)

admin.site.register(Reports)


# changing the admin site header

admin.site.site_header = "Clinic Management System Administrator"

admin.site.site_title = "CMS Administrator"

admin.site.index_title = "CMS Administrator"


# removing the default group model from the admin site

admin.site.unregister(Group)
