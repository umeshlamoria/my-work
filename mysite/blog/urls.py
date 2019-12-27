from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
	path('post/<str:slug>/edit/',views.post_edit,name='post_edit'),
	path('user/<int:pk>/edit/',views.user_edit,name='user_edit'),
	path('post/tag/<str:slug>/',views.tags,name='tag'),
	path('post/categories/<str:slug>',views.categorys,name='category'),
	path('post/list/',views.post_list,name='post_list'),
	path('post/new/',views.post_new,name='post_new'),
	path('user/list/',views.user_list,name='user_list'),
	path('user/<int:pk>/',views.user_detail,name='user_detail'),
	path('post/<str:slug>/',views.post_detail,name='post_detail'),
	path('register/',views.register,name='register'),
	path('logout/',views.logout_request,name='logout'),
	path('login/',views.login_request,name='login'),
	path('',views.home,name='home'),
]