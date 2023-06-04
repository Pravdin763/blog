from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post


class PostView(View):
    '''Вывод записи'''
    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        return render(request, 'website/blog.html', {'post_list': posts})

class PostDetail(View):
    """Отдельная страница записи"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'website/blog_detail.html', {'post': post})