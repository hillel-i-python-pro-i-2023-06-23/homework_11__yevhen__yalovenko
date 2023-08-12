from django.views.generic import TemplateView

from apps.homework.services.generate_humans import generate_humans


class GenerateHumansView(TemplateView):
    template_name = "homework/generate_humans.html"

    def get_context_data(self, amount: int = 25, **kwargs):
        context = super().get_context_data(**kwargs)

        humans = generate_humans(amount=amount)

        context.update(
            humans=humans,
        )

        return context
