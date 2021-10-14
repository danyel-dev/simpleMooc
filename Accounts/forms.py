from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('já existe usuário com este email')
        else:
            return email


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class EditAccountForm(forms.ModelForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('já existe usuário com este email')
        else:
            return email


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        