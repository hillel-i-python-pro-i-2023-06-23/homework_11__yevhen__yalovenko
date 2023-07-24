from django.http import HttpResponse


def home_page(request):
    return HttpResponse(
        "Hi. This is homepage. Welcome!"
        "<br>If you want, you can enter your 'name' and amount of variants, then"
        "we generate example of possible user name and email in 'get-users/' section</br>"
    )
