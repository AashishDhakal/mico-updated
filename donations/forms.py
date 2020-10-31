from django import forms
from .models import CausesDonation
from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html


class CausesDonationForm(forms.ModelForm):
    
    class Meta:
        model = CausesDonation
        fields = '__all__'


class ExtPayPalPaymentsForm(PayPalPaymentsForm):
    def render(self):
        form_open  = u'''<form action="%s" method="post">''' % (self.get_endpoint())
        form_close = u'</form>'
        # format html as you need
        submit_elm = u'''<input type="submit" class="btn btn-primary" value="Proceed to paypal securely">'''
        return format_html(form_open+self.as_p()+submit_elm+form_close)

