from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="this number must contain 8 dights.",
)

# Create your models here.
class User(AbstractUser):
    pass 

class Specialty(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 

class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialties = models.ManyToManyField(
        Specialty,
        related_name='doctors',
        
    )
def validate_birth_date(v):
    if v>= timezone.localdate():
        raise ValidationError(
            "La date de naissance n'est pas valide"
        )

class Patient(User):
    national_id = models.CharField(max_length=8,unique=True, validators=[
        RegexValidator(
            regex=r'^\d{8}$',
            message="this number must contain 8 dights.",)
                                                                        
                                                                        ])
       
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)