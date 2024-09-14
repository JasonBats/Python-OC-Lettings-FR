from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models

"""
Defines models for the 'lettings' app, including Address and Letting.
"""


class Address(models.Model):
    """
    Represents a physical address with the following components:

    — number: The street number.
    — street: The name of the street.
    — city: The city where the address is located.
    — state: The state or region (abbreviation) of the address.
    — zip_code: The postal code for the address.
    — country_iso_code: The ISO 3166-1 alpha-3 country code.

    The string representation returns the full address in the format “number — street”.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a letting (property) with the following attributes:

    — title: The title or name of the property.
    — address: A one-to-one relationship with the Address model,
    representing the location of the property.

    The string representation returns the title of the property.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
