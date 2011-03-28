from django.http import HttpResponse
from django.shortcuts import render_to_response

from blog.models import Tag

import urllib
import simplejson

def tags():
    tags = Tag.objects.all()
    for tag in tags:
        tag.count = len(tag.post_set.all())
    return render_to_response('widgets/tags.html', {'tags': tags})

def twitter():
    USERNAME = 'zachtib'
    s = urllib.urlopen('http://twitter.com/status/user_timeline/%s.json' \
        '?count=10' % USERNAME).read()
    o = simplejson.loads(s)
    return render_to_response('widgets/twitter.html', {'tweets': o})



def load(request, widget):
    try:
        return globals()[widget]()
    except KeyError:
        return HttpResponse('Could not locate widget: %s' % widget)
