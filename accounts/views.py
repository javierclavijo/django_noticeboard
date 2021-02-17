from django.shortcuts import render, get_object_or_404
from .forms import UserCreationExtendedForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.models import User


# Create your views here.
class RegistrationFormView(FormView):
    form_class = UserCreationExtendedForm
    template_name = 'registration/registration.html'
    success_url = 'done/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'registration/registration-success.html'


class UserProfileView(DetailView):
    model = User

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
