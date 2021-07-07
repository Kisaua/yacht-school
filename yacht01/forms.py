from .models import Contact
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': Contact._meta.get_field('name').help_text, 'class' : 'form-control', 'id' : 'name'}),
            'user_email': EmailInput(attrs={'placeholder': Contact._meta.get_field('user_email').help_text, 'class' : 'form-control', 'id' : 'email'}),
            'subject': TextInput(attrs={'placeholder': Contact._meta.get_field('subject').help_text, 'class' : 'form-control','id' : 'Subject'}),
            'message': Textarea(attrs={'placeholder': Contact._meta.get_field('message').help_text, 'class' : 'form-control', 'rows': '5'},)
        }
