from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^tags/(?P<slug>[\w-]+)/$', TagsDetail.as_view(), name='tag_detail'),
]