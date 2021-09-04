from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


# Create your models here.
class ApiModel(models.Model):

    filename = models.CharField(_("filename"), max_length=100)
    x_axis_180 = models.IntegerField(_("x_axis_180"))
    y_axis_90 = models.IntegerField(_("y_axis_90"))
    diagonal_45 = models.IntegerField(_("diagonal_45"))
    diagonal_135 = models.IntegerField(_("diagonal_135"))
    all = models.IntegerField(_("all"))
    none = models.IntegerField(_("none"))

