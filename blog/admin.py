from blog.models import Post, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'author', 'text']

    def get_form(self, req, obj=None, **kwargs):
        self.current_user = req.user
        return super(PostAdmin, self).get_form(req, obj, **kwargs)

    def formfield_for_dbfield(self, field, **kwargs):
        from django import forms
        from django.contrib.auth import models
        if field.name == 'author':
            queryset = models.User.objects.all()
            return forms.ModelChoiceField(
                queryset=queryset, initial=self.current_user.id)
        return super(PostAdmin, self).formfield_for_dbfield(field, **kwargs)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'author', 'text']

admin.site.register(Comment, CommentAdmin)
