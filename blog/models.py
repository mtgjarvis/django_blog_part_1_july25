from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} {self.author}'
