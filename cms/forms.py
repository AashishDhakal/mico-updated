from django import forms
from cms.models import Contact, Endowment, WorkWithUs, Sponsorship

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name','email_address','subject','message']

class EndowmentForm(forms.ModelForm):

    class Meta:
        model = Endowment
        fields = ['name', 'email', 'endowment_type']


class WorkwithusForm(forms.ModelForm):
    
    class Meta:
        model = WorkWithUs
        fields= ['first_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'state_province', 'postal_code','country', 'email_address', 'subject', 'message',]


class SponsorshipForm(forms.ModelForm):
    
    class Meta:
        model = Sponsorship
        fields= ['first_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'state_province', 'postal_code','country', 'email_address', 'subject', 'message',]
