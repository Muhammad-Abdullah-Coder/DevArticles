from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import Article

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
