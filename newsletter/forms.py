from django import forms
from .models import SignUp

# Here we dont need a model
class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain in ['gmail', 'hotmail', 'yahoo']:
               raise forms.ValidationError("Please use a valid free email (hotmail/gmail/yahoo)")
        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']
        # exclude = ['full_name'] -> don't use this

    # check the info before sending to db.
    # 'clean_' overrides the 'email'
    def clean_email(self):
        # gets the email(clean, beautiful way) from the instance of the form
        email = self.cleaned_data.get('email')
        # splits the email in at the '@' in two variables
        email_base, provider = email.split('@')
        # splits the provider variable (e.g. 'hotmail.com') in two
        domain, extension = provider.split('.')
        # checks this, and raise ValidationError if true (not)
        """if not domain in ['gmail', 'hotmail', 'yahoo']:
               raise forms.ValidationError("Please use a valid free email (hotmail/gmail/yahoo)")"""
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # if len(full_name.split())==1:
        #     raise forms.ValidationError("Please enter your full name")
        return full_name
