from django.views import generic
from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    all_posts = Post.objects.filter(status=1).order_by('-created_on')
    latest_post = Post.objects.filter(status=1).order_by('-created_on').first()
    return render(request, 'index.html', {'latest_post': latest_post, 'post_list': all_posts})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'