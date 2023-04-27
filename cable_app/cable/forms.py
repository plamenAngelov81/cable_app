from django import forms

from cable_app.cable.models import Cable, Order


class CableCreateForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name', 'cap_number', 'clutch_number', 'inductor_type', 'machine']


class CableEditForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name', 'cap_number', 'clutch_number', 'inductor_type', 'machine']


class OrderCable(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'cable', 'company_name', 'cable_quantity']
