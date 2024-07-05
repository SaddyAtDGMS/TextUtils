from django.contrib import admin

# Register your models here.

from .models import Minemast,  Coscode, Distcode, Mnlcode, Ownmast, Pincode, States,  Rgncode, Srgncode,  Users, Zonecode


# Register your models here.
admin.site.register(Minemast)
admin.site.register(Coscode)
admin.site.register(Distcode)
admin.site.register(Mnlcode)
admin.site.register(Ownmast)
admin.site.register(Pincode)
admin.site.register(Rgncode)
admin.site.register(Srgncode)
admin.site.register(States)
admin.site.register(Users)
admin.site.register(Zonecode)
