from django.contrib.auth.models import User
from django.db import models

categories = (
    ("politiques", "politiques"),
    ("economies", "economies"),
    ("security", "security"),
    ("sovereignty", "sovereignty"),
    ("other", "other")
)


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_viral = models.BooleanField(default=False)
    is_viewable = models.BooleanField(default=True)
    is_about_sovereignty = models.BooleanField(default=False)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=categories, max_length=60, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def getUrl(self):
        return self.image.url


class ArticleWIthVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)