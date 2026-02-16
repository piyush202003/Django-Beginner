from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse  
from .models import Blog
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-updated_at')
    return render(request, 'blogging/index.html',{'blogs':blogs})

def blogDetails(request, pk):
    blogs = Blog.objects.get(pk = pk)
    return render(request, 'blogging/blogDetails.html', {'blogs':blogs})

def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloggingIndex')
    else:
        form = BlogForm()
    return render(request, 'blogging/createBlog.html', {'form':form})

def editBlog(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('bloggingIndex')
    form = BlogForm(instance = blog)
    return render(request, 'blogging/editBlog.html', {'form':form})

def deleteBlog(request, pk):
    blog = Blog.objects.get(pk = pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('bloggingIndex')
    return render(request, 'blogging/deleteBlog.html', {'blog':blog})

