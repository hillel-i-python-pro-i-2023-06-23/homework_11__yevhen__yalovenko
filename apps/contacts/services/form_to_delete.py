from django import forms
from django.core.validators import RegexValidator
from apps.contacts.models import Contact


class FormToDelete(forms.ModelForm):
    id_validator = RegexValidator(r"^\d+$", "Id must contains only digits.")

    id = forms.CharField(validators=[id_validator])

    class Meta:
        model = Contact
        fields = ["id"]
