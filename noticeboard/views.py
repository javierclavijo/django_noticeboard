from django.shortcuts import render
from django.views import generic
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notice
from .forms import NewNoteForm


# Create your views here.


class ActiveNoticesView(generic.ListView):
    def get_queryset(self):
        """Return only the notices which have not expired yet"""
        return Notice.objects.filter(exp_date__gt=Now()).order_by('exp_date', 'title')
    model = Notice
    extra_context = {
        'title': 'Active Notices'
    }


class ExpiredNoticeView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        """Return only the notices which have expired"""
        return Notice.objects.filter(exp_date__lte=Now()).order_by('-exp_date', 'title')
    model = Notice
    extra_context = {
        'title': 'Expired Notices'
    }


class SingleNoticeView(generic.DetailView):
    model = Notice


class NewNoticeView(LoginRequiredMixin, generic.CreateView):
    form_class = NewNoteForm
    template_name = 'noticeboard/notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
