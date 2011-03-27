from django.contrib.syndication.views import Feed
from django.template.defaultfilters import slugify

from blog.models import Post

class LatestPostsFeed(Feed):
    title = 'zachtib.com/blog'
    link = '/blog/'
    description = ''

    def items(self):
        return Post.objects.order_by('-postdate')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return '/blog/%d/%s/' % (item.id, slugify(item.title))

    def item_pubdate(self, item):
        return item.postdate
