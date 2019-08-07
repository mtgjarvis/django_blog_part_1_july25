from django.db import models
from django.forms import ModelForm, DateInput
from datetime import date
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(1)])
    draft = models.BooleanField(default=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Article')

    def __str__(self):
        return f"{self.title}"


class DateInput(DateInput):
    input_type = 'date'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date', 'author', 'user']
        widgets = {'published_date': DateInput(), }

    def clean(self):
        cleaned_data = super().clean()

        pub_date = cleaned_data.get('published_date')
        today = date.today()
        if cleaned_data.get('draft'):
            if pub_date <= today:
                self.add_error(
                    'published_date', 'Draft articles must have a future date')
        else:
            if pub_date > today:
                self.add_error(
                    'published_date', 'Published articles must have current date')


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']