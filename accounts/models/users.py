from typing import Any
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    '''
    This is a user manager for authenticating users with email instead of username    
    '''

    def create_user(self, email, password, **extra_fields):
        '''
        this is for authenticating and save users with email and password.
        '''

        if not email :
            raise ValueError (_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        '''
        this is for authenticating and save superusers with email and password.
        '''

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff'))
        return self.create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom User Model for authentication management through email instead of username.
    '''    

    email = models.EmailField(max_length= 255, unique= True)
    is_superuser = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_verified = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    create_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email