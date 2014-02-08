from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
    url(r'^chats/', include('chat.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
