from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import datetime

from blog.models import Post, Comment, Tag

def index(request):
    latest_post_list = Post.objects.all().order_by('-postdate')[:5]
    return render_to_response('blog/index.html', {'latest_post_list': latest_post_list})

def post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    c = Comment.objects.filter(post=post_id).order_by('date')
    return render_to_response('blog/post.html', {'post': p, 'comments': c},
                                context_instance=RequestContext(request))

def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:
        ct = request.POST['comment']
    except KeyError:
        return render_to_response('blog/post.html', {
            'post': p,
            'error_message': 'An error occurred.',
        }, context_instance=RequestContext(request))
    c = Comment(post=p, text=ct)
    c.save()
    return HttpResponseRedirect(reverse('blog.views.post', args=(p.id,)))


def tag(request, tag_id):
    t = get_object_or_404(Tag, pk=tag_id)
    p = t.post_set.all()
    return render_to_response('blog/tag.html', {'tag': t, 'posts': p})
