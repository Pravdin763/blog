from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post, Likes
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

def get_client_ip(request):
    x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward:
        ip = x_forward.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class Addlikes(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class Dislike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
