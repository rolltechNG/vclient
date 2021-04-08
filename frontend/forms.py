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
