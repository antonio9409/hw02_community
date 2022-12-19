from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from .consts import numbers_posts


def index(request):
    posts = Post.objects.all()[:numbers_posts]
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {'posts': posts,
               'title': title
               }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
#    posts = Post.objects.filter(group=group).order_by('-pub_date')[:numbers_posts]
    posts = posts.groups.all()
    posts = Post.objects.filter(pub_date__year=1854)
    template = 'posts/group_list.html'
    title = f'Записи сообщества {group}'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
