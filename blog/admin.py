from blog.models import Post, Comment, Tag
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'tags', 'text']
    list_display = ['title', 'author', 'get_tags', 'postdate', 'editdate']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

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
    fields = ['post', 'author', 'name', 'email', 'text']
    list_display = ['get_author', 'get_email', 'post', 'date']

admin.site.register(Comment, CommentAdmin)

admin.site.register(Tag)
