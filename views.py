from django.http.response import HttpResponse
from django.shortcuts import render


posts = [
    {
        'author': 'Toshe',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Sashka',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    },
]


def home(request):

    context ={
     'posts':posts
    }

    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
