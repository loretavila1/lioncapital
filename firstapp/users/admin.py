from django.contrib import admin
from .models import User, Asesor, Logro
# Register your models here.
admin.site.register(User) #registrar el modelo para tener el crud desde admin
admin.site.register(Asesor)
admin.site.register(Logro)
