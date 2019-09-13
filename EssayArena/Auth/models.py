import jwt

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, timedelta
from django.conf import settings


class User(AbstractBaseUser):
    ADMIN = "ADMIN"
    WRITER = "WR"
    CLIENT = "CL"
    USER_ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (WRITER, "Writer"),
        (CLIENT, "Client")
    ]
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()

    @property
    def token(self):
        expiry_date = datetime.now() + timedelta(hours=24)
        payload = {
            'email': self.email,
            'exp': int(expiry_date.strftime('%s'))
        }
        token = jwt.encode(payload, settings.SECRET_KEY)

        return token.decode('utf-8')



