from django.contrib import admin
from hotels.models import Location,Hotel,Room,Client,Order,Booked

# Register your models here.	

admin.site.register(Hotel)
admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Order)
admin.site.register(Booked)
admin.site.register(Client)
