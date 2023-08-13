from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom user model"""
    username = models.CharField(max_length=150, unique=True)
    portal_login = models.CharField(max_length=30, blank=True, null=True)
    portal_password = models.CharField(max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
