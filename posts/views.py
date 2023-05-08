from django.shortcuts import render,redirect
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, SignUpForm
# this library is used for debugging
import pdb

# Create your views here.

# def home(request):
#     recent_posts = Post.objects.all().order_by('-created_date')
#     return render(request, 'home.html', {'posts': recent_posts})


# def layout(request):
#     return render(request, 'layout.html')

# class HomeView(ListView):
#
#     model = Post
#     template_name = 'home.html'
#     success_url = reverse_lazy('/')
#     context_object_name = 'posts'


#Method1
# class PostListView(LoginRequiredMixin,View):
#     def get(self, request):
#         recent_posts = Post.objects.all()
#         return render(request, 'posts.html', {'posts': recent_posts})


#Method2
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'
    success_url = reverse_lazy('list_posts')
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

# decorator for only authenticated users
# @login_required
# def posts(request):
#     # filter posts to list only for login in user
#     p = Post.objects.filter(author=request.user)
#     return render(request, 'posts.html', {'posts': p})

# Function Based Views
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


# Class Based views
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['title', 'text', 'image', 'is_featured']
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    fields = ['title','text', 'image', 'is_featured']
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('list_posts')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
