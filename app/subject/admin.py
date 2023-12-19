from django.contrib import admin
from .models.address import Address
from .models.subject import Person, Company, Bailiff

# Register your models here.
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Bailiff)
