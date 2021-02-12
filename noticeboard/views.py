from django.shortcuts import render
from django.views import generic
from django.db.models.functions import Now

from .models import Notice


# Create your views here.


class ActiveNoticesView(generic.ListView):
    def get_queryset(self):
        """Return only the notices which have not expired yet"""
        return Notice.objects.filter(exp_date__gt=Now())

    model = Notice


class ExpiredNoticeView(generic.ListView):
    def get_queryset(self):
        """Return only the notices which have not expired yet"""
        return Notice.objects.filter(exp_date__lte=Now())

    model = Notice


class SingleNoticeView(generic.DetailView):
    model = Notice
