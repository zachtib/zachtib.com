from django.http import HttpResponse
from django.shortcuts import render_to_response

from blog.models import Tag

from urllib import urlopen
import simplejson

def tags():
    tags = Tag.objects.all()
    for tag in tags:
        tag.count = len(tag.post_set.all())
    return render_to_response('widgets/tags.html', {'tags': tags})

def twitter():
    USERNAME = 'zachtib'
    u = urlopen('http://twitter.com/status/user_timeline/%s.json' % USERNAME)
    j = simplejson.loads(u.read())
    f = [ t for t in j if not t['text'].startswith('@') ][:5]
    return render_to_response('widgets/twitter.html', {'tweets': f})

def load(request, widget):
    try:
        return globals()[widget]()
    except KeyError:
        return HttpResponse('Could not locate widget: %s' % widget)
