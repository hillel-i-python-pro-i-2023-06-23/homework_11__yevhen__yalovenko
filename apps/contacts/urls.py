from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
]
