from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contact_list"),
    path("create/", views.ContactCreateView.as_view(), name="contacts_create"),
    path("update/<int:pk>/", views.ContactUpdateView.as_view(), name="contacts_update"),
    path("delete/<int:pk>/", views.ContactDeleteView.as_view(), name="contacts_delete"),
    path("delete/", views.delete_all_contacts_view, name="contacts_delete"),
]
