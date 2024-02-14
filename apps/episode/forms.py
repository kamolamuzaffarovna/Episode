from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'name', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'comment_input comment_textarea',
            'placeholder': 'Message',
            'required': 'required'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'comment_input',
            'type': 'text',
            'placeholder': 'Name',
            'required': 'required'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'comment_input',
            'type': 'image',
            'placeholder': 'Image',
            'required': 'required'
        })
