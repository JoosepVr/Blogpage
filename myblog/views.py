from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def home(request):
    recent_posts = Post.objects.all().order_by('-created_date')
    return render(request, 'home.html', {'posts': recent_posts})

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')