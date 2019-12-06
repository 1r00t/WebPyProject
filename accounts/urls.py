from django.urls import path

from accounts.views import SignUp, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<int:pk>/edit/', ProfileUpdateView.as_view(), name='edit-profile')
]