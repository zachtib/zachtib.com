from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    postdate = models.DateTimeField('Post Date', auto_now_add=True)
    editdate = models.DateTimeField('Edit Date', auto_now=True)
    text = models.TextField('Post Text')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    post = models.ForeignKey(Post)
    text = models.TextField('Comment Text')
    date = models.DateTimeField('Post Time', auto_now_add=True)

    def __unicode__(self):
        return 'Comment by %s on %s' % (self.author, self.post)
