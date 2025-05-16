from django.contrib import admin
from .models import Question
from .models import BlogPost

admin.site.register(BlogPost)
admin.site.register(Question)
