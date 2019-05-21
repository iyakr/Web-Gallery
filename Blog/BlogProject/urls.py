from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path('', PostsAll.as_view()),
    path('Posts/<int:pk>/', PostsDetail.as_view()),
    path('MyPosts/', UserPost.as_view()),
    # path('Likes/', Like.as_view()),
]













# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.ShowPostView.as_view(), name='blog-home'),
#     path('user/<str:username>/', views.UserAllPostsView.as_view(), name='user-post'),
#     path('news/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
#     path('news/<int:pk>/update/', views.UpdatePostView.as_view(), name='post-update'),
#     path('news/<int:pk>/delete/', views.DeletePostView.as_view(), name='post-delete'),
#     path('news/add/', views.CreatePostView.as_view(), name='post-add'),
#     path('contacts/', views.contacts, name='blog-contacts'),
# ]
