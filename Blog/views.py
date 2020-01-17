from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from Blog.forms import PostForm, BlogForm, QuestionForm
from Blog.models import Post, Blog, Question


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse("post-list", args=(self.request.user.username,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs.get('slug'))
        blog = Blog.objects.get(user=user)
        return self.model.objects.filter(blog=blog)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = self.kwargs.get('slug')
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog-list')

    def get_success_url(self):
        return reverse("post-detail", args=(self.object.pk,))

    def form_valid(self, form):
        blog = Blog.objects.get(user=self.request.user)
        form.instance.blog = blog
        return super().form_valid(form)


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('blog-list')

    def get_success_url(self):
        return reverse("post-detail", args=(self.object.post.pk,))

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)
