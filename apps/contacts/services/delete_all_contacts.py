from apps.contacts.models import Contact


def delete_all_contacts():
    queryset = Contact.objects.all()
    queryset.delete()
