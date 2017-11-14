from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MyModel


admin.site.register(MyModel, MarkdownxModelAdmin)


#from  web.models import *

#admin.site.register(Menu, MarkdownxModelAdmin)
