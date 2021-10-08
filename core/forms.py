from django import forms


class ContactCourse(forms.Form):

    def clean(self):
        data = self.cleaned_data

        nome = data.get('name')
        
        if len(nome) < 6:
            self.add_error('name', 'quantidade de caracteres muito poucos')


    name = forms.CharField(label='Nome', max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
 