from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

def all_blog(request):
    blog=Blog.objects.all()
    return render(request,"blog/all_blogs.html",{"blogs":blog})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,"blog/detail.html",{"blog":blog})
