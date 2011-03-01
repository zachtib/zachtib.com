from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    postdate = models.DateTimeField('Post Date')
    editdate = models.DateTimeField('Edit Date')
    text = models.TextField('Post Text')
