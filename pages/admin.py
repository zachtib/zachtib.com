from pages.models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
admin.site.register(Page, PageAdmin)
