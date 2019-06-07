from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from portfolio.models import *
from blog.models import *
from .forms import *
from django.core.mail import EmailMessage
from django.http import Http404


class Home(DetailView):
    model = Page
    template_name='page/index.html'
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
        context['form'] = ContactForm
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
        context['form'] = ContactForm
        assert isinstance(context, object)
        return context

class FeedBack(CreateView):
    model = FeedBack
    form_class = FeedBackAdd
    success_url = '/success'

def success(request):
    return render(request, 'page/success.html')


def feedback(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            name = request.POST.get(
                'name'
            , '')
            phone = request.POST.get(
                'phone'
            , '')
            email = EmailMessage(
                'Письмо с сайта kmv-it.ru',
                name + ' ' + phone,
                'justscoundrel@yandex.ru',
                ['justscoundrel@yandex.ru',],
                headers={'Message-ID': 'foo'},
)
            email.send()
            return redirect('success')
        else:
            raise Http404

    return redirect('home')
