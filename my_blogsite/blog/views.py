from django.shortcuts import render


posts = [
    {
        'author': 'Corey',
        'title': 'Blog_post01',
        'content': 'First post content',
        'date_posted': 'Dec 03, 2018'
    },
    {
        'author': 'rvdw',
        'title': 'Blog_post02',
        'content': 'Second post content',
        'date_posted': 'Dec 01, 2017'
    }
]


def home_view(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html')
