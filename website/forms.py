from captcha.fields import CaptchaField
from django import forms

from website.models import Contact


class ContactForm(forms.ModelForm):
    Subject = forms.CharField(max_length=255, empty_value=None, required=False)
    captcha = CaptchaField()

    class Meta:
        model = Contact
        exclude = ['Created date']
        fields = "__all__"
