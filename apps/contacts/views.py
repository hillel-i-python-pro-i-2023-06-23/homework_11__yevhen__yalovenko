from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contacts.models import Contact
from apps.contacts.services.delete_all_contacts import delete_all_contacts


class ContactsListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )

    success_url = reverse_lazy("contacts:contact_list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "name",
        "phone",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context

    success_url = reverse_lazy("contacts:contact_list")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:contact_list")


def delete_all_contacts_view(request):
    delete_all_contacts()

    return redirect(reverse_lazy("contacts:contact_list"))
