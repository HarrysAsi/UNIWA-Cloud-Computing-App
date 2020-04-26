from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    """
    Model which represents the user model,
    username is set to None because Email is used as username
    """

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _("user's")

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



