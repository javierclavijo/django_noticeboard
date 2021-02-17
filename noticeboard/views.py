from django.shortcuts import render
from django.views import generic
from django.db.models.functions import Now
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notice


# Create your views here.


class ActiveNoticesView(generic.ListView):
    def get_queryset(self):
        """Return only the notices which have not expired yet"""
        return Notice.objects.filter(exp_date__gt=Now())

    context_object_name = 'active_notices_list'

    model = Notice


class ExpiredNoticeView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        """Return only the notices which have expired"""
        return Notice.objects.filter(exp_date__lte=Now())

    model = Notice


class SingleNoticeView(generic.DetailView):
    model = Notice
