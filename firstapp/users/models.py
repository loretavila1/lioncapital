from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
    
# Create your models here.
class User(AbstractUser): #AbstractUser te pone por default un formulario, aún así, puedo agregar más campos
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=10, null=True)
    photo = models.ImageField(null=True)
    pass


class Asesor(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)


    def __str__(self):
        return self.name

class Logro(models.Model):
    STATUS = (
        ('No iniciado', 'No iniciado'),
        ('Iniciado', 'Iniciado'),
        ('Completado', 'Completado'),
    )

    asesor = models.ForeignKey(Asesor, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200, null=True)
    cantidad = models.IntegerField(default=0, null=True) 
    data_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name