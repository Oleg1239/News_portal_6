from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    list_filter = ('user',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_type', 'created_time', 'title', 'rating')
    list_filter = ('author', 'post_type', 'categories')
    search_fields = ('title', 'content')

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('post', 'category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_time', 'rating')
    list_filter = ('post', 'user')
    search_fields = ('text',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
