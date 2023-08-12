from django import forms
from django.core.validators import RegexValidator
from apps.contacts.models import Contact


class FormToSearch(forms.ModelForm):
    search_validator = RegexValidator(r"^[a-zA-Z0-9+]{1,13}$", "Test.")

    search = forms.CharField(validators=[search_validator])

    class Meta:
        model = Contact
        exclude = ["id", "name", "phone", "created_at", "modified_at"]
