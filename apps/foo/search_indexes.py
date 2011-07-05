import datetime
from haystack.indexes import *
from haystack.sites import SearchSite

site = SearchSite()

from armstrong.apps.articles.models import Article


class ArticleIndex(SearchIndex):
    title = EdgeNgramField(document=True, model_attr="title")
    type = EdgeNgramField()
    pub_date = DateTimeField(model_attr='pub_date')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Article.objects.filter(pub_date__lte=datetime.datetime.now())

    def prepare_type(self, obj):
        return "article"


site.register(Article, ArticleIndex)
