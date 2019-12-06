from django import forms

from Blog.models import Post, Blog, Question


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'type']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'user': forms.HiddenInput(),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']