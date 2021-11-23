from django.shortcuts import render
from posts.models import Posts

def index(request):
    queryset = Posts.objects.filter(featured = True)
    return render(request, 'index.html', {
        'object_list':queryset
    })

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})