from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.feeds import LatestPostsFeed

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    # Example:
    # (r'^zachtib_com/', include('zachtib_com.foo.urls')),
    (r'^$', 'home.views.index'),
    (r'^login/$', 'backend.views.backend_login'),
    (r'^logout/$', 'backend.views.backend_logout'),
    (r'^register/$', 'backend.views.register'),

    (r'^blog/$', 'blog.views.index'),
    (r'^blog/feed/', LatestPostsFeed()),
    (r'^blog/post/(?P<post_id>\d+)/$', 'blog.views.post'),
    (r'^blog/post/(?P<post_id>\d+)/comment/$', 'blog.views.comment'),
    (r'^blog/tag/(?P<tag_name>\w+)/$', 'blog.views.tag'),

    (r'^blog/archive/$', 'blog.views.archive'),
    (r'^blog/archive/(?P<year>\d+)/$', 'blog.views.archive'),
    (r'^blog/archive/(?P<year>\d+)/(?P<month>\d+)/$', 'blog.views.archive'),
    (r'^blog/archive/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'blog.views.archive'),

    (r'^blog/page/(?P<page>\d+)/$', 'blog.views.archive'),

    (r'^resume/$', 'resume.views.index'),

    (r'^widget/(?P<widget>\w+)/$', 'widgets.views.load'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^(?P<page_name>\w+)/$', 'pages.views.render'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
