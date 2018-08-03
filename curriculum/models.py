from django.db import models
from django.utils import timezone



class Estudio(models.Model):
    carrera= models.CharField(max_length=200)
    lugar= models.CharField(max_length=200)
    sede= models.CharField(max_length=200)
    comienzo = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.carrera
    

class Experiencia(models.Model):
    trabajo= models.CharField(max_length=200)
    descripcion=models.TextField()
    lugar= models.CharField(max_length=200)
    comienzo = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.trabajo

class Lenguajes(models.Model):
    nombre= models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
