from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', srm_home, name='srm_home'),
    url(r'^orders/$', OrderList.as_view(), name='order_list'),
    url(r'^contacts/$', ContactList.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^contact/(?P<pk>\d+)/edit$', ContactEdit.as_view(), name='contact_edit'),
    url(r'^contact/(?P<pk>\d+)/delete$', ContactDelete.as_view(), name='contact_delete'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^add/$', OrderAdd.as_view(), name='order_add'),
    url(r'^(?P<pk>\d+)/edit$', OrderEdit.as_view(), name='order_edit'),
    url(r'^(?P<pk>\d+)/delete$', OrderDelete.as_view(), name='order_delete'),
    url(r'^filter/$', order_filter, name='order_filter'),
]
