from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post

def index(request):
    latest_post_list = Post.objects.all().order_by('-postdate')[:5]
    return render_to_response('blog/index.html', {'latest_post_list': latest_post_list})

def post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render_to_response('blog/post.html', {'post': p})
