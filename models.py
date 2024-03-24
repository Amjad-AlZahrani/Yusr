from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, username, name, age, sex, password=None):
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(username=username, name=name, age = age, sex = sex)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, name, age, sex,  password):
        user = self.create_user(username, name, age, sex, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','age', 'sex']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.username
