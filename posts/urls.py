from django.urls import path
from .views import *

urlpatterns = [
 path('', HomeView.as_view(), name='home'),
 path('posts/', PostListView.as_view(), name='posts'),
 path('create/', PostCreateView.as_view(), name='post_create'),
 path('accounts/signup/', UserCreateView.as_view(), name='signup'),
 path('create/', post_create, name='post_create'),
 path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
 path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
 path("newlayout/", NewlayoutView.as_view(), name="newlayout")
]
