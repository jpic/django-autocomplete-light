__author__ = 'heddevanderheide'

import autocomplete_light.shortcuts as autocomplete_light

from django import forms
from django.contrib import admin

from .models import XModel, YModel, ZModel


class YModelForm(forms.ModelForm):
    x = autocomplete_light.ModelChoiceField('XModelAutocomplete', label="XModel")

    class Meta:
        exclude = tuple()
        model = YModel


class YModelAdmin(admin.ModelAdmin):
    form = YModelForm


admin.site.register(XModel)
admin.site.register(YModel, YModelAdmin)
