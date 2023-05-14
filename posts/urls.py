from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
 path('', PostListView.as_view(), name='list_posts'),
 path('api/', include(router.urls)),
 path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
 path('create/', PostCreateView.as_view(), name='post_create'),
 path('accounts/signup/', UserCreateView.as_view(), name='signup'),
 #path('create/', post_create, name='post_create'),
 path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
 path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]