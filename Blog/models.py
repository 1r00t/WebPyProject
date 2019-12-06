from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    TYPE_CHOICES = (
        ('A', "Breaking News!"),
        ('B', "Followup"),
        ('C', "Just kidding!"),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)