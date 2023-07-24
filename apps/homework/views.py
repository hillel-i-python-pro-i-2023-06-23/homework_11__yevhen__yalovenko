from django.http import HttpResponse

from apps.homework.services.processing_users import format_users, output_user_info


def generate_users(request, name: str = "User", amount: int = 100):
    formatted_users = format_users(amount)
    output = output_user_info(formatted_users)
    return HttpResponse(
        f"Hello {name}. We generate {amount} variants of users name and email for you: <ol>{output}</ol>"
    )
