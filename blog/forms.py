from django import forms

class AnonymousCommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.widgets.Textarea)

class AuthenticatedCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.widgets.Textarea)
