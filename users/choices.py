from django.db import models


class UserTypeChoices(models.TextChoices):
    PetOwner = 'PetOwner'
    Servicer = 'Servicer'
    Shelter = 'Shelter'