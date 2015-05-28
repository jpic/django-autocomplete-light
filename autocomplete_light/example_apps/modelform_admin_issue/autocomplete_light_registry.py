__author__ = 'heddevanderheide'

import autocomplete_light.shortcuts as autocomplete_light

from .models import XModel


class XModelAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['x']

autocomplete_light.register(XModel, XModelAutocomplete, attrs={
    'placeholder': "Enter xmodel",
    'data-autocomplete-minimum-characters': 1
})
