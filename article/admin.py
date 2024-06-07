from django.contrib import admin
from .models import Article, ArticleWIthVideo


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "is_viral", "is_viewable", "image", "user",
                    "category", "date_published", "date_modified"]


class ArticleWithVideoAdmin(admin.ModelAdmin):
    list_display = ["title", "video", "description", "user", "status", "date_published", "date_modified"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleWIthVideo, ArticleWithVideoAdmin)
