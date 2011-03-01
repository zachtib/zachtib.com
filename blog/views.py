from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World')

def post(request, post_id):
    return HttpResponse('Viewing post %s' % post_id)
