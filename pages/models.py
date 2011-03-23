from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField('Page Text', blank=True)

    def __unicode__(self):
        return self.title
