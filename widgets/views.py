from django.http import HttpResponse
from django.shortcuts import render_to_response

from blog.models import Tag

def tags():
    tags = Tag.objects.all()
    for tag in tags:
        tag.count = len(tag.post_set.all())
    return render_to_response('widgets/tags.html', {'tags': tags})

def load(request, widget):
    try:
        return globals()[widget]()
    except KeyError:
        return HttpResponse('Could not locate widget: %s' % widget)
