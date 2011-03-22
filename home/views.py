from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Post

def index(request):
    try:
        post = Post.objects.get(postdate=Post.objects.aggregate(
            Max('postdate'))['postdate__max'])
    except ObjectDoesNotExist:
        pass
    except MultipleObjectsReturned:
        pass

    return render_to_response('home/index.html', locals(),
            context_instance=RequestContext(request))
