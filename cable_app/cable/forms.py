from django import forms

from cable_app.cable.models import Cable, Order


class CableCreateForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name',
                  'cap_number',
                  'clutch_number',
                  'inductor_type',
                  'machine'
                  ]
        widgets = {
            'cable_name': forms.TextInput(attrs={
                'placeholder': 'Enter Cable Name',
            }),
            'cap_number': forms.TextInput(attrs={
                'placeholder': 'Enter Cap Number',
            }),
            'clutch_number': forms.TextInput(attrs={
                'placeholder': 'Enter Clutch Number',
            }),
            'inductor_type': forms.Textarea(attrs={
                'cols': 21,
                "rows": 3,
                'placeholder': 'Enter Inductor Type',
            }),
            'machine': forms.Textarea(attrs={
                'cols': 21,
                "rows": 3,
                'placeholder': 'Enter Machine',
            }),
        }


class CableEditForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_name',
                  'cap_number',
                  'clutch_number',
                  'inductor_type',
                  'machine'
                  ]


class OrderCable(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user',
                  'cable',
                  'company_name',
                  'cable_quantity'
                  ]


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['confirm_user',
                  'is_confirmed'
                  ]

