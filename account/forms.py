from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import UserBody

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Last Name'
        })
    )

    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Username'
        })
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Password Again'
        })
    )

    age = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Age'
        })
    )

    height = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Height (cm)'
        })
    )

    weight = forms.DecimalField(
        label='',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Weight (kg)',
            'step': '0.01'
        })
    )

    gender = forms.ChoiceField(
        label='',
        choices=UserBody.gender_choices,
        widget=forms.RadioSelect
    )

    physical_activity = forms.ChoiceField(
        label='',
        choices=UserBody.activity_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.pop('autofocus', None)



class SignInForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Username'
        })
    )
    
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Password'
        })
    )



class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Last Name'
        })
    )
    
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Username'
        })
    )

    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
        )



class UpdateUserPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'New Password'
        })
    )
    
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'New Password Again'
        })
    )

    class Meta:
        model = User
        fields = (
            'new_password1',
            'new_password2'
        )



class UpdateUserBodyForm(forms.ModelForm):
    age = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Age'
        })
    )
    
    height = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Height (cm)'
        })
    )
    
    weight = forms.DecimalField(
        label='',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-control-lg rounded-3',
            'placeholder': 'Your Weight (kg)',
            'step': '0.01'
        })
    )
    
    gender = forms.ChoiceField(
        label='',
        choices=UserBody.gender_choices,
        widget=forms.RadioSelect
    )
    
    physical_activity = forms.ChoiceField(
        label='',
        choices=UserBody.activity_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = UserBody
        fields = (
            'age',
            'height',
            'weight',
            'gender',
            'physical_activity'
        )
