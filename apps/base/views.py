from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="Hello! This is Human Wonka fabrics homepage. We will generate as many human as you wish",
            #
            title="Home Page",
        )

        return context
