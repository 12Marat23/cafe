from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mail_text', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'mail_text', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'mail_text', 'placeholder': 'Your Phone'}),
            'message': forms.Textarea(
                attrs={'class': 'massage-bt', 'placeholder': 'Massage', 'rows': 5, 'id': 'comment'}),
        }
