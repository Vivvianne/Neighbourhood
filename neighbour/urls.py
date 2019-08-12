from django.urls import path
from . import views
from django.conf import settings
from .views import PostListView, PostUpdateView, PostDeleteView, PostDetailView,UserPostListView


urlpatterns = [
    path('home/', PostListView.as_view() , name= 'neighbour-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_save, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.about, name='neighbour-about'),
    path('business/new/', views.business, name='business-form'),
    path('business/', views.business, name='business'),
    path('neighbourhood/new/', views.business, name='neighbourhood-form'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
]

    