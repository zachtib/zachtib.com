from pages.models import Page
from backend.forms import LoginForm

def processor(request):
    pages = Page.objects.all()
    login_form = LoginForm()
    return locals()
