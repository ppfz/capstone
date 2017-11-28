from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from web.models import *

admin.site.register(Order, MarkdownxModelAdmin)
