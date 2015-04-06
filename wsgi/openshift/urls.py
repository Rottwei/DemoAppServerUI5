from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'views.upload', name='upload'),
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^upload', 'openshift.views.upload_file', name='upload_file'),
    url(r'^read', 'openshift.views.read_file', name='read_file'),
    url(r'^create', 'openshift.views.create_table', name='create_table'),
    url(r'^sync', 'openshift.views.sync_file', name='sync_file'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^upload/', 'views.upload', name='upload'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
