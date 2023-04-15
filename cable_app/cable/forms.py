from django import forms

from cable_app.cable.models import Cable


class CableCreateForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name', 'cap_number', 'clutch_number', 'inductor_type', 'machine']


class CableEditForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name', 'cap_number', 'clutch_number', 'inductor_type', 'machine']