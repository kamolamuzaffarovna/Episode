from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'type': 'text',
            'class': 'contact_input',
            'required': 'required',
            'placeholder': 'Name'
        })
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'contact_input',
            'required': 'required',
            'placeholder': 'E-Mail'
        })
        self.fields['subject'].widget.attrs.update({
            'type': 'text',
            'class': 'contact_input',
            'placeholder': 'Subject'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'contact_input contact_textarea',
            'required': 'required',
            'placeholder': 'Message'
        })