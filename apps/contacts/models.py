from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text="Contact phone number")

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

    class Meta:
        ordering = ["modified_at", "name"]
