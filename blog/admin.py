from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'author', 'postdate', 'editdate', 'text']
admin.site.register(Post, PostAdmin)
