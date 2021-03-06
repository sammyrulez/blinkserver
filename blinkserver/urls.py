from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blinkserver.views.home', name='home'),
    # url(r'^blinkserver/', include('blinkserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^hook/(?P<hook_name>\w+)','blinkserver.core.views.hook', name='public_hook'),
    url(r'^admin/stop_blink/$','blinkserver.core.views.stop_blink', name="stop_blink"),
    url(r'^privatehook/(?P<hook_name>\w+)','blinkserver.core.views.private_hook'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

)
