from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^zachtib_com/', include('zachtib_com.foo.urls')),
    (r'^$', 'home.views.index'),
    (r'^blog/$', 'blog.views.index'),
    (r'^blog/post/(?P<post_id>\d+)/$', 'blog.views.post'),
    (r'^blog/post/(?P<post_id>\d+)/comment/$', 'blog.views.comment'),
    (r'^blog/tag/(?P<tag_id>\d+)/$', 'blog.views.tag'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
