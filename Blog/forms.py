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


class SearchForm(forms.Form):
    query = forms.CharField(label="Suche", max_length=100)
    opt_blog = forms.BooleanField(label="Blog", required=False)
    opt_post = forms.BooleanField(label="Posts", required=False)
    opt_ques = forms.BooleanField(label="Questions", required=False)