# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Profile


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog-list')
    template_name = 'signup.html'


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    fields = ['info']
    success_url = reverse_lazy('blog-list')

