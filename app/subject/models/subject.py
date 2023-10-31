""" Subject model class with extend class"""
from django.db import models
from .address import Address


class Subject(models.Model):
    creating_date = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


    class Meta:
        abstract = True


class Person(Subject):
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='imię')
    last_name = models.CharField(max_length=60, null=True, verbose_name='nazwisko')
    pesel = models.CharField(max_length=11, null=True, blank=True, verbose_name='numer pesel')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='numer telefonu')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(Subject):
    name = models.CharField(max_length=300, null=True, blank=True, verbose_name='pełna nazwa podmiotu gospodarczego')
    nip = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='nip')
    krs = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='notatki')

    def __str__(self):
        return f'{self.name}'