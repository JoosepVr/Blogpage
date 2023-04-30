from django.shortcuts import render,redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
# this library is used for debugging
import pdb

# Create your views here.

def home(request):
    recent_posts = Post.objects.all().order_by('-created_date')
    return render(request, 'home.html', {'posts': recent_posts})

# decorator for only authenticated users
@login_required
def posts(request):
    # filter posts to list only for login in user
    p = Post.objects.filter(author=request.user)
    return render(request, 'posts.html', {'posts': p})

# Function Based Views
# @login_required
# def post_create(request):
#     if request.method == 'POST':
#         pdb.set_trace()
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('posts')
#     else:
#         form = PostForm()
#     return render(request, 'create_post.html', {'form': form})

# Class Based views
class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title','text']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title','text']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')
