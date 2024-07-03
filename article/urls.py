from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from .views import ArticleListView, DetailArticle, click_image


urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('article_detail/<slug:pk>', DetailArticle.as_view(), name="detail_article"),
    path('clicked_image', click_image, name="clicked_image"),
    #path('article/<name: str>/<id: urlsafe_base64_encode(str(1).encode("utf-8"))>')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)