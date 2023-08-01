from django.db.models import Q
from django.shortcuts import render
from apps.contacts.models import Contact
from apps.contacts.services.form_to_search import FormToSearch


def search_contact(request):
    if request.method == "POST":
        form = FormToSearch(request.POST)
        if form.is_valid():
            searched_value = form.cleaned_data["search"]
            try:
                contact = Contact.objects.get(Q(id=searched_value) | Q(name=searched_value) | Q(phone=searched_value))
                return render(request, "contacts/contact_details.html", {"contact": contact})
            except Contact.DoesNotExist:
                form.add_error("search", "Contact with this id, name or phone does not exits")

    else:
        form = FormToSearch()

    return render(request, "contacts/search_contact.html", {"form": form})
