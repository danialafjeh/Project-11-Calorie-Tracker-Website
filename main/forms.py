from django import forms
from .models import FoodIntake
from decimal import Decimal

class FoodIntakeForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Food name'
        })
    )

    quantity = forms.DecimalField(
        label='',
        max_value=Decimal('5000'),
        max_digits=6,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Quantity',
            'step': '0.01'
        })
    )

    unit = forms.ChoiceField(
        label='',
        choices=FoodIntake.unit_choices,
        widget=forms.RadioSelect
    )

    calories_per_unit = forms.DecimalField(
        label='',
        max_value=Decimal('2000'),
        max_digits=7,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Calories ( kcal per 100g, piece, 100mL )',
            'step': '0.01'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        unit = cleaned_data.get('unit')
        if quantity is not None and unit == 'piece':
            if quantity != quantity.to_integral_value():
                self.add_error(
                    'quantity',
                    'Quantity must be a whole number when the unit is piece.'
                )
        return cleaned_data
