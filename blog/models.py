from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    postdate = models.DateTimeField('Post Date', auto_now_add=True)
    editdate = models.DateTimeField('Edit Date', auto_now=True)
    text = models.TextField('Post Text')
    tags = models.ManyToManyField(Tag)

    def get_tags(self):
        return ', '.join([unicode(t) for t in self.tags.all()])
    get_tags.short_description = 'Tags'

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    post = models.ForeignKey(Post)
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField('Comment Text')
    date = models.DateTimeField('Post Time', auto_now_add=True)

    def get_author(self):
        if self.author is not None:
            return unicode(self.author)
        elif self.name is not None:
            return self.name
        return 'Anonymous'
    get_author.short_description = 'Author'

    def get_email(self):
        if self.author is not None:
            return self.author.email
        elif self.email is not None:
            return self.email
        return 'Unknown'
    get_email.short_description = 'Email'

    def __unicode__(self):
        return 'Comment by %s on %s' % ((self.get_author), self.post)
