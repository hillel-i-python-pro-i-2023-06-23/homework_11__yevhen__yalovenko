from django.shortcuts import render, redirect

from apps.contacts.models import Contact
from apps.contacts.services.form_to_update import ContactFormToUpdate


def update_contact(request):
    if request.method == "POST":
        form = ContactFormToUpdate(request.POST)
        if form.is_valid():
            contact_phone = form.cleaned_data["phone"]
            try:
                contact = Contact.objects.get(phone=contact_phone)
                contact.name = form.cleaned_data["new_name"]
                contact.phone = form.cleaned_data["new_phone"]
                contact.save()
                return redirect("contacts:contacts_list")
            except Contact.DoesNotExist:
                form.add_error("phone", "Contact with this phone does not exist.")
    else:
        form = ContactFormToUpdate()

    return render(request, "contacts/update_contact.html", {"form": form})
