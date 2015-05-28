__author__ = 'heddevanderheide'

from django.db import models


class XModel(models.Model):
    x = models.CharField(max_length=12)

    def __str__(self):
        return self.x


class YModel(models.Model):
    x = models.ForeignKey(XModel)
    y = models.CharField(max_length=12)

    def __str__(self):
        return self.y


class ZModel(models.Model):
    y = models.ForeignKey(YModel)
    z = models.CharField(max_length=12)

    def __str__(self):
        return self.z
