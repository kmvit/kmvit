from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from page.models import *


class PortfolioList(ListView):
    model = Portfolio
    def get_context_data(self, **kwargs):
        context = super(PortfolioList, self).get_context_data(**kwargs)
        context['whatwedo'] = Whatwedo.objects.all()
        assert isinstance(context, object)
        return context
        
class PortfolioDetail(DetailView):
    model = Portfolio
    