from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


def directory_path(instance, filename):
    return f'images/user/{instance.username}/{filename}'


class User(AbstractUser):
    image = models.ImageField(verbose_name=_('picture'), upload_to=directory_path, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('user:user-detail', kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.username