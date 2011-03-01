from blog.models import Post, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'author', 'postdate', 'editdate', 'text']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'author', 'date', 'text']

admin.site.register(Comment, CommentAdmin)
