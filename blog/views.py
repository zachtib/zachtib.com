from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import datetime

from blog.models import Post, Comment, Tag
from blog.forms import AuthenticatedCommentForm, AnonymousCommentForm

def index(request):
    posts = Post.objects.all().order_by('-postdate')[:5]
    for post in posts:
        post.comment_count = len(Comment.objects.filter(post=post.id))
    return render_to_response('blog/index.html', {'latest_post_list': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id).order_by('date')
    if request.user.is_authenticated():
        logged_in_msg = 'Commenting as %s' % unicode(request.user)
        form = AuthenticatedCommentForm()
    else:
        form = AnonymousCommentForm()
    return render_to_response('blog/post.html', locals(),
                                context_instance=RequestContext(request))

def archive(request, year=None, month=None, day=None, page=None):
    if year is not None and month is not None and day is not None:
        posts = Post.objects.filter(postdate__year=year,
                                        postdate__month=month,
                                        postdate__day=day)
    elif year is not None and month is not None:
        posts = Post.objects.filter(postdate__year=year,
                                        postdate__month=month)
    elif year is not None:
        posts = Post.objects.filter(postdate__year=year)
    elif page is not None:
        posts = Post.objects.all()
    return render_to_response('blog/index.html', {'latest_post_list': posts})

def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = AuthenticatedCommentForm(request.POST)
            if form.is_valid():
                cn = form.cleaned_data['name']
                ce = form.cleaned_data['email']
                ct = form.cleaned_data['comment']
                c = Comment(post=p, name=cn, email=ce, text=ct)
                c.save()
                return HttpResponseRedirect(
                    reverse('blog.views.post', args=(p.id,)))
        else:
            pass
    else:
        if request.user.is_authenticated():
            form = AuthenticatedCommentForm()
        else:
            form = AnonymousCommentForm()
    cs = Comment.objects.filter(post=post_id).order_by('date')
    return render_to_response('blog/post.html',
        {'post': p, 'comments': cs, 'error_message': 'An error occurred.',
        'form': form},
        context_instance=RequestContext(request))

def tag(request, tag_name):
    t = get_object_or_404(Tag, name=tag_name)
    p = t.post_set.all()
    return render_to_response('blog/tag.html', {'tag': t, 'posts': p})
