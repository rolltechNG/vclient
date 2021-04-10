import re

from django import forms


class NINPostForm(forms.Form):
    """Form for a user to verify NIN"""
    nin = forms.CharField(required=True, help_text='e.g. 123xxxxxxxx')

    # check if the nin is a valid one
    def clean_nin(self):
        nin = self.cleaned_data['nin']
        regex = re.compile("^[0-9]{11}$")
        if not regex.match(nin):
            raise forms.ValidationError("NIN is incorrect.")

        return nin


class PhonePostForm(forms.Form):
    """Form for a user to verify Phone Number"""
    phone_number = forms.CharField(required=True, help_text='e.g. 080xxxxxxxx')

    # check if the phone number is a valid one
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        regex = re.compile("^[0]\d{10}$")
        if not regex.match(phone_number):
            raise forms.ValidationError("Phone number is incorrect")

        return phone_number


class DemoPostForm(forms.Form):
    """Form for a user to verify Demo"""
    nin = forms.CharField(required=True, help_text='e.g. 123xxxxxxxx')

    # check if the nin is a valid one
    def clean_nin(self):
        nin = self.cleaned_data['nin']
        regex = re.compile("^[0-9]{11}$")
        if not regex.match(nin):
            raise forms.ValidationError("NIN is incorrect.")

        return nin
