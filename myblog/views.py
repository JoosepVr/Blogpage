from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from posts.forms import SignUpForm
from posts.models import Post

class HomeView(ListView):
    """    def get(self,request):
        recent_post = Post.objects.all().order_by("-created_date")
        return render(request, 'home.html', {'posts': recent_post})"""
    # decorator for only authenticated user
    model = Post
    template_name = "home.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"

class AboutView(ListView):
    model = Post
    template_name = 'about_me.html'
    success_url = reverse_lazy("about_me")
    context_object_name = "posts"


class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)