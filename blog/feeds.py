from django.contrib.syndication.views import Feed

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
        return '/blog/post/%d/' % item.id
