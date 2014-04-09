from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.http import HttpResponse
from example.tasks import loop_forever


def start_celery_task(request, *args, **kwargs):
    loop_forever.apply_async()
    return HttpResponse('Task started.  Try to set a breakpoint in example.tasks.loop_forever().')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', start_celery_task, name='home'),
)
