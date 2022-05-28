from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def home(request):
    return render(request, 'blog/home.html')


def post_detail(request, slug):
    return render(request, 'blog/post_detail.html')
