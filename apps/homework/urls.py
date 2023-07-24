from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
    path("get-users/", views.generate_users, name="generate_users"),
    path("get-users/<name>/", views.generate_users, name="generate_users"),
    path("get-users/<name>/<int:amount>/", views.generate_users, name="generate_users"),
]
