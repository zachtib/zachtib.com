from django.shortcuts import render_to_response, get_object_or_404

from pages.models import Page

def render(request, page_name):
    page = get_object_or_404(Page, title__iexact=page_name)
    return render_to_response('pages/page.html', {'page': page})
