from django.shortcuts import render, reverse, HttpResponse ,HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .forms import *
from urllib.request import Request, urlopen
from urllib.parse import quote
from datetime import datetime
from django.db.models import Count, Sum
# Create your views here.

# Create your views here.
@login_required
def srm_home(request):
    return render(request, 'srm/index.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        login(request, user)
        # Перенаправление на "правильную" страницу
        return render(request,'masters/index.html')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")


def logout_view(request):
    logout(request)
    return redirect('home')


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Deal

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['sum'] = Deal.objects.all().aggregate(total_sum=Sum('budget'))
        return context


@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Deal


@method_decorator(login_required, name='dispatch')
class OrderAdd(CreateView):
    model = Deal
    form_class = OrderAddForm
    def get_success_url(self):
        return reverse('orders:order_list')

@method_decorator(login_required, name='dispatch')
class OrderEdit(UpdateView):
    model = Deal
    form_class = OrderEditForm
    template_name = 'srm/deal_edit.html'

    def get_success_url(self):
        return reverse('orders:order_list')


@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Deal
    success_url = reverse_lazy('orders:order_list')


@method_decorator(login_required, name='dispatch')
class ContactList(ListView):
    model = Contact

@method_decorator(login_required, name='dispatch')
class ContactDetail(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        context['deal_list'] = Deal.objects.filter(contact=self.object)
        return context

@method_decorator(login_required, name='dispatch')
class ContactEdit(UpdateView):
    model = Contact
    form_class = ContactEditForm
    template_name = 'srm/contact_edit.html'

    def get_success_url(self):
        return reverse('orders:contact_list')


@method_decorator(login_required, name='dispatch')
class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('orders:contact_list')

@login_required
def order_filter(request):
    """Фильтр заказов"""
    if 'select' in request.GET and request.GET['select']=='all':
        order_list = Deal.objects.all()
    else:
        order_list = Deal.objects.filter(stage__title = request.GET.get('select'))
    context = {'deal_list':order_list}
    return render(request, 'srm/deal_list.html', context)
