from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


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

class AddComment(View):
    """Добавление комментариев"""
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')