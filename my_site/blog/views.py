from datetime import date
from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Post, Author, Tag
# Create your views here.
# posts = [
#     {
#         "slug": "hike-in-the-mountain",
#         "image": "mountains.jpg",
#         "author": "Ashish",
#         "date": date(2022, 5, 28),
#         "title": "Mountain hiking",
#         "excerpt": "Mountains are bitchin",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque, ipsam eius maxime iste nesciunt blanditiis neque, velit ex dicta possimus nobis ipsa dignissimos inventore eligendi rerum temporibus quos, iusto in.Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque, ipsam eius maxime iste nesciunt blanditiis neque, velit ex dicta possimus nobis ipsa dignissimos inventore eligendi rerum temporibus quos, iusto in.Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque, ipsam eius maxime iste nesciunt blanditiis neque, velit ex dicta possimus nobis ipsa dignissimos inventore eligendi rerum temporibus quos, iusto in.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Maximilian",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#          Woods are my favrt place to be.
#          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#         """
#     }
# ]


# def get_date(post):
#     return post['date']


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


def home(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identify_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': identify_post,
                                                     "post_tags": identify_post.tags.all(),
                                                     })
