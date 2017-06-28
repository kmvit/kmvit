from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', Page.as_view(), name='page'),
]
