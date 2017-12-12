from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from page.views import *
from srm.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^filer/', include('filer.urls')),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),   
    url(r'^accounts/login/$', auth_views.login),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),
    url(r'^feedback/', FeedBack.as_view(), name='feedback'),
    url(r'^success/', success, name='success'),
    url(r'^srm/', include('srm.urls', namespace='orders', app_name='orders')),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^(?P<slug>[\w-]+)/$', PageDetail.as_view(), name='page'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
