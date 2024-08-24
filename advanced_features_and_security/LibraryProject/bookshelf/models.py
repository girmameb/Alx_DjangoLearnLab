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
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", _("Can view article")),
            ("can_create", _("Can create article")),
            ("can_edit", _("Can edit article")),
            ("can_delete", _("Can delete article")),
        ]