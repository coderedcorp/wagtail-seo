from django.views.generic import DetailView

from .models import MySnippet


class MySnippetDetailView(DetailView):
    model = MySnippet
    template_name = MySnippet.template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["self"] = context["object"]
        return context
