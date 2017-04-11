from django import forms
from .models import Visite


class VisiteAmbulatorioForm(forms.Form):
    visite = forms.ModelChoiceField(
        queryset=None,
        empty_label='Scegli visita',
        # widget=forms.RadioSelect,
        required=False
    )
    tutti = forms.BooleanField(required=False)