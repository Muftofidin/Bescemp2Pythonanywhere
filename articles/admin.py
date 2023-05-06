from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInLIne(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLIne]

admin.site.register(Article)
admin.site.register(Comment)
