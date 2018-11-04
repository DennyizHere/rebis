from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import F
from . models import Post
from django.http import HttpResponseRedirect

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body',] 

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['body',]
    template_name = 'post_edit.html'

def increment_counter(request, pk):
    post = Post.objects.get(pk=pk)
    post.votes = F('votes') + 1
    post.save()
    return HttpResponseRedirect('/')

def increment_money(request, pk):
    post = Post.objects.get(pk=pk)
    post.tips = F('tips') + 5
    post.save()
    return HttpResponseRedirect('/')

def confirm(request, pk):
    post = Post.objects.get(pk=pk)
    post.done = True
    post.save()
    return HttpResponseRedirect('/')
