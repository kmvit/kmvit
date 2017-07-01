from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from portfolio.models import *
from blog.models import *
from .forms import *



class Home(DetailView):
    model = Page

    def get_object(self, queryset=None):
        page = get_object_or_404(Page, id=1)
        return page

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['whoweare'] = Whoweare.objects.first()
        context['whatwedo'] = Whatwedo.objects.all()
        context['lastwork'] = Lastwork.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['fact']= Fact.objects.all()
        context['review'] = Review.objects.all()
        context['blog'] = Blog.objects.all()
        assert isinstance(context, object)
        return context



class PageDetail(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
        context['whoweare'] = Whoweare.objects.first()
        context['whatwedo'] = Whatwedo.objects.all()
        context['lastwork'] = Lastwork.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['fact']= Fact.objects.all()
        context['review'] = Review.objects.all()
        context['blog'] = Blog.objects.all()
        assert isinstance(context, object)
        return context

class FeedBack(CreateView):
    model = FeedBack
    form_class = FeedBackAdd
    success_url = '/'