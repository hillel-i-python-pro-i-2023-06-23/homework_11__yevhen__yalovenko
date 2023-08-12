from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
    path("create/", views.create_contact, name="create_contact"),
    path("search/", views.search_contact, name="search_contact"),
    path("update/", views.update_contact, name="update_contact"),
    path("delete/", views.delete_contact, name="delete_contact"),
]
