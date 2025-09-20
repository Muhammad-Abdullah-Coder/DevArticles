from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CoustomUserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class = CoustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(DjangoLoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
