from django.contrib import admin

# Register your models here.
from .models import ServiceProvider,Client,NewUser

admin.site.register(Client)
admin.site.register(ServiceProvider)
admin.site.register(NewUser)
