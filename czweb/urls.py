from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from czoo import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        views.index, name='index'),

    url(r'categories/(?P<category>\w+)/$',
        views.view_category, name='view_category'),

    # url(r'^$', 'czweb.views.home', name='home'),
    # url(r'^czweb/', include('czweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
