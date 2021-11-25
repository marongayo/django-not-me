from django.shortcuts import render
from posts.models import Posts

def index(request):
    featured = Posts.objects.filter(featured = True)
    latest = Posts.objects.order_by('-timestamp')[0:3]

    return render(request, 'index.html', {
        'object_list':featured,
        'latest':latest
    })

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})