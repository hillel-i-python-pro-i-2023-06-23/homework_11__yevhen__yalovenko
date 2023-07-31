from django.shortcuts import render, redirect

from apps.contacts.services.contact_form import ContactForm


def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:contacts_list")
    else:
        form = ContactForm()

    return render(request, "contacts/create_contact.html", {"form": form})
