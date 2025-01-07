# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    race = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Colorgroup(models.Model):

    #__Colorgroup_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Colorgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Colorgroup")
        verbose_name_plural = _("Colorgroup")


class Color(models.Model):

    #__Color_FIELDS__
    color_group = models.ForeignKey(ColorGroup, on_delete=models.CASCADE)

    #__Color_FIELDS__END

    class Meta:
        verbose_name        = _("Color")
        verbose_name_plural = _("Color")



#__MODELS__END
