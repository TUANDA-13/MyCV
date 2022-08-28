from . import models
from django.forms import ModelForm,TextInput,Textarea
class EmailForm(ModelForm):
    class Meta:
        model = models.Mail
        fields = ['name','email','phone','subject','message',]
        widgets = { 
            'name': TextInput(attrs={'class':'contact_name', 'placeholder':'Name'}),
            'email': TextInput(attrs={'class':'contact_email', 'placeholder':'Email'}),
            'phone': TextInput(attrs={'class':'contact_phone', 'placeholder':'Phone'}),
            'subject': TextInput(attrs={'class':'contact_subject', 'placeholder':'Subject'}),
            'message': Textarea(attrs={'class':'contact_message', 'placeholder':'Message','rows':4}),
        }