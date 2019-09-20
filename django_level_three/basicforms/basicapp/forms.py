from django import forms
from django.core import validators

def check_for_z(value):  ##use the keyword 'value' as an argument for custom validation functions
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with a Z')

class NameForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email addresses must match")