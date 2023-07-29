from collections.abc import Iterator

from apps.contacts.models import Contact
from apps.homework.services import faker


def generate_contact() -> Contact:
    return Contact(
        name=faker.unique.name(),
        phone=f"+380{faker.unique.msisdn()[4:]}",
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
