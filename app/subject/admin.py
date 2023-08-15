from django.contrib import admin
from .models.adress import Adress
from .models.subject import Person, Company

# Register your models here.
admin.site.register(Adress)
admin.site.register(Person)
admin.site.register(Company)

