from django.shortcuts import render, redirect

from apps.contacts.models import Contact
from apps.contacts.services.form_to_delete import FormToDelete


def delete_contact(request):
    if request.method == "POST":
        form = FormToDelete(request.POST)
        if form.is_valid():
            contact_id = form.cleaned_data["id"]
            try:
                contact = Contact.objects.get(id=contact_id)
                contact.delete()
                return redirect("contacts:contacts_list")
            except Contact.DoesNotExist:
                form.add_error("id", "Contact with this id does not exist.")
    else:
        form = FormToDelete()

    return render(request, "contacts/delete_contact.html", {"form": form})
