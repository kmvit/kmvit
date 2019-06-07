from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from page.models import *
from page.forms import *


class PortfolioList(ListView):
    model = Portfolio
    def get_context_data(self, **kwargs):
        context = super(PortfolioList, self).get_context_data(**kwargs)
        context['whatwedo'] = Whatwedo.objects.all()
        assert isinstance(context, object)
        return context

class PortfolioDetail(DetailView):
    model = Portfolio
    def get_context_data(self, **kwargs):
        context = super(PortfolioDetail, self).get_context_data(**kwargs)
        context['form'] = ContactForm
        assert isinstance(context, object)
        return context
