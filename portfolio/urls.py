from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PortfolioList.as_view(), name='portfolio_list'),
    url(r'^(?P<slug>[\w-]+)/$', PortfolioDetail.as_view(), name='portfolio_detail'),
]
