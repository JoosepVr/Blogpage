from django.urls import path
from .views import *

urlpatterns = [
 path('', HomeView.as_view(), name='home'),
 path('posts/', PostView.as_view(), name='posts'),
 path('create/', PostCreateView.as_view(), name='post_create'),
 path('accounts/signup/', UserCreateView.as_view(), name='signup'),
 path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
 path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
 path("new_layout/", NewlayoutView.as_view(), name="new_layout")
]
