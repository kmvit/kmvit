from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', srm_home, name='srm_home'),
    
    url(r'^tasks/$', TaskList.as_view(), name='task_list'),
    url(r'^task/(?P<pk>\d+)/$', TaskDetail.as_view(), name='task_detail'),
    url(r'^task/add/$', TaskAdd.as_view(), name='task_add'),
    url(r'^task/(?P<pk>\d+)/edit$', TaskEdit.as_view(), name='task_edit'),
    url(r'^task/(?P<pk>\d+)/delete$', TaskDelete.as_view(), name='task_delete'),
    
    url(r'^contacts/$', ContactList.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^contact/(?P<pk>\d+)/edit$', ContactEdit.as_view(), name='contact_edit'),
    url(r'^contact/(?P<pk>\d+)/delete$', ContactDelete.as_view(), name='contact_delete'),
    
    url(r'^orders/$', OrderList.as_view(), name='order_list'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^add/$', OrderAdd.as_view(), name='order_add'),
    url(r'^(?P<pk>\d+)/edit$', OrderEdit.as_view(), name='order_edit'),
    url(r'^(?P<pk>\d+)/delete$', OrderDelete.as_view(), name='order_delete'),
    url(r'^filter/$', order_filter, name='order_filter'),
]
