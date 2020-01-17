from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from Blog.forms import PostForm, BlogForm, QuestionForm, SearchForm
from Blog.models import Post, Blog, Question

from django.db.models import Q


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


def search_view(request):
    form = SearchForm(request.POST)
    context = {}
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            query = form.cleaned_data.get("query")
            opt_blog = form.cleaned_data.get("opt_blog")
            opt_post = form.cleaned_data.get("opt_post")
            opt_ques = form.cleaned_data.get("opt_ques")

            if opt_blog:
                blogs = Blog.objects.filter(
                    Q(title__contains=query) | Q(description__contains=query)
                )
                context["blogs"] = blogs

            if opt_post:
                posts = Post.objects.filter(
                    Q(title__contains=query) | Q(text__contains=query)
                )
                context["posts"] = posts

            if opt_ques:
                quests = Question.objects.filter(text__contains=query)
                context["quests"] = quests

            print(context)

    return render(request, "Blog/search.html", {"form": form, "context": context})