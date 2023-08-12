from django.urls import path, include

from apps.homework import views

app_name = "homework"

urlpatterns = [
    path(
        "generate-humans/",
        include(
            [
                path("<int:amount>/", views.GenerateHumansView.as_view(), name="generate_humans_with_amount"),
                path("", views.GenerateHumansView.as_view(), name="generate_humans"),
            ]
        ),
    ),
]
