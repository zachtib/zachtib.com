from pages.models import Page

def processor(request):
    pages = Page.objects.all()
    return locals()
