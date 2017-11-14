from django.db import models

from markdownx.models import MarkdownxField


class MyModel(models.Model):
    myfield = MarkdownxField()

# Create your models here
