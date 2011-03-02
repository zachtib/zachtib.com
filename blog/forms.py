from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.widgets.Textarea)

