from django.db import models
from django.contrib.auth.models import AbstractUser

class CoustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='coustomuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='coustomuser_set',
        blank=True,
    )

    def __str__(self):
        return self.username
