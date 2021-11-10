from django import forms

from .models import Reply


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('reply',)

    reply = forms.CharField(label='Responder', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '5'}
    ))
