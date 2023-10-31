from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=60,
                            default='',
                            verbose_name='ulica')
    house_number = models.CharField(max_length=10, default='', verbose_name='nr. domu / lokalu')
    city = models.CharField(max_length=60, default="Grudziądz", verbose_name='miejscowość')
    postcode = models.CharField(max_length=60, default='86-300', verbose_name='kod pocztowy')

    class Meta:
        unique_together = ('street', 'house_number', 'city', 'postcode')

