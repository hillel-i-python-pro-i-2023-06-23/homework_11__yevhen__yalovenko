import secrets
from typing import NamedTuple
from collections.abc import Iterator

from apps.homework.services import faker


class Human(NamedTuple):
    username: str
    email: str
    password: str

    def __str__(self):
        return f"{self.username} {self.email} {self.password}"


def generate_human() -> Human:
    user_name = faker.unique.user_name()
    suffix = faker.random_int(0, 999)
    login = f"{user_name}_{suffix}"
    safe_password = secrets.token_urlsafe(16)
    email_domain = faker.domain_name()
    return Human(
        username=f"Username: {login}",
        email=f"Email: {user_name}{suffix}@{email_domain}",
        password=f"Password: {safe_password}",
    )


def generate_humans(amount: int) -> Iterator[Human]:
    for _ in range(amount):
        yield generate_human()
