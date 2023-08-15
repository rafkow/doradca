from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin


class UserManager(UserManager):

    def create_user(self, username, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """Creates and saves a new super user"""
        user = self.create_user(username=username, password=password, **extra_fields)
        user.save(using=self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    """"Custom user model"""
    portal_login = models.CharField(max_length=30, blank=True, null=True)
    portal_password = models.CharField(max_length=30, blank=True, null=True)


