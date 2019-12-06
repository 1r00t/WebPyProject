from django.contrib.auth.decorators import login_required
from django.urls import path

from Blog import views
from Blog.views import PostDetailView, PostCreateView, PostListView, QuestionCreateView

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('blog/create/', login_required(views.BlogCreateView.as_view()), name='blog-create'),

    #path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', login_required(PostCreateView.as_view()), name='post-create'),
    path('<str:slug>/', PostListView.as_view(), name='post-list'),

    path('<int:post_id>/question/create/', login_required(QuestionCreateView.as_view()), name='question-create'),
]
