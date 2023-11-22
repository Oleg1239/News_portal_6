from django import forms
from .models import Post, News

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']  # Убедитесь, что список полей соответствует вашей модели Post.
        # Поле 'post_type' исключается, чтобы установить его в представлении в зависимости от URL.

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text']  # Убедитесь, что список полей соответствует вашей модели News.

# Убедитесь, что в вашей модели News также есть поле author, если оно должно быть редактируемым.
