from django import forms
from django.core.validators import EmailValidator
from crispy_forms.helper import FormHelper
from .models import Issue
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Login'
        }
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))


class AddIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title',
                  'email',
                  'priority',
                  'status',
                  'description']