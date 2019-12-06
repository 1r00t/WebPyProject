from django.contrib import admin

# Register your models here.
from Blog.models import Post, Blog, Question, Answer

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Question)
admin.site.register(Answer)