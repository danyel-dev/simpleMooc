from django import forms
from django.contrib.auth import get_user_model

from Courses.models import Comment

User = get_user_model()


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['As senhas não conferem'],
            )
        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')


class EditAccountForm(forms.ModelForm):
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']

    #     if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
    #         raise forms.ValidationError('já existe usuário com este email')
    #     else:
    #         return email

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
