from django.http import HttpResponse

def load(request, widget):
    try:
        return locals()[widget]()
    except KeyError:
        return HttpResponse('Could not locate widget: %s' % widget)

