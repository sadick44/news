from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from .models import Article, ArticleWIthVideo

"""
    The View is a class based view, it is used to get more than one query_set unlike ListView which is for just one queryset.
    ArticleListView displays all the viewable articles, article with views and even viral/scandal event articles
"""


class ArticleListView(View):
    template_name = "home.html"
    context = {}

    def get(self, request, *args, **kwargs):
        daily_news = Article.objects.filter(is_viewable=True)
        try:
            limited_daily = daily_news[:4]
        except:
            print('There are less than 4 articles, make sure you have at least 4 articles')

        articleWithVideos = ArticleWIthVideo.objects.filter(status=True)
        self.context = {'daily_news': daily_news, 'articleWithVideos': articleWithVideos,
                        'limited_daily': limited_daily, 'first_image': daily_news[:1]}

        return render(request, self.template_name, self.context)


class DetailArticle(DetailView):
    model = Article
    template_name = "detail_article.html"
    context_object_name = "article"


def click_image(request):
    return HttpResponse("An image is clickec")