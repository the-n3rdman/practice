from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('posts/', views.home, name = 'home'),
    path('posts/<slug>', views.post_detail, name = 'post_detail')

]
