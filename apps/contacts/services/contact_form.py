from django import forms
from django.core.validators import RegexValidator
from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    name_validator = RegexValidator(
        r"^[a-zA-Z]{1,100}$", "Name must contain only letters and be no longer than 100 characters."
    )
    phone_validator = RegexValidator(r"^\+[0-9]{12}$", 'Phone must start with a "+" and contain exactly 12 digits.')

    name = forms.CharField(validators=[name_validator])
    phone = forms.CharField(validators=[phone_validator])

    class Meta:
        model = Contact
        fields = ["name", "phone"]