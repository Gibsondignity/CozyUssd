from django.contrib import admin
from .models import User, AppartmentLocation, Booking
# Register your models here.

admin.site.register(User)
admin.site.register(Booking)
admin.site.register(AppartmentLocation)

