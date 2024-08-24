from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager  # Import the custom manager


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()  # Assign the custom manager

from django.contrib.auth.models import BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        #extra_fields.setdefault('is_staff', True)
       # extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password)