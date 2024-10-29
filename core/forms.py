
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']  # Fields included in the form
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message...'}),  # Customization for the message field
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'subject': 'Subject',
            'message': 'Message',
        }

    def clean_email(self):  # Email validation
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):  # Check for a specific domain, for example
            raise forms.ValidationError('Please provide a valid email address.')
        return email
