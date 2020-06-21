from bootstrap_modal_forms.generic import BSModalUpdateView
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from bootstrap_modal_forms.forms import BSModalForm
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


from .models import Issue, Comments


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', 'issue', 'user')

        widgets = {
            'issue': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }


class UpdateIssueForm(BSModalForm):
    class Meta:
        model = Issue
        fields = ['priority',
                  'status']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'company', 'password1', 'password2']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

