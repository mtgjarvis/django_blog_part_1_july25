from django.db import models
from django.forms import ModelForm


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} {self.author}"


class ArticleForm(ModelForm):
    model = Article
    fields = ['title', 'body', 'draft', 'published_date', 'author']