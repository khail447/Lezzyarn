"""lezzyarn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from core.views import frontpage,signup
from feed.views import feed, search
from yarnerprofile.views import edit_profile, follows, followers, unfollow_yarner, follow_yarner, yarnerprofile

from feed.api import api_add_yarn, api_add_like
urlpatterns = [


    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),


    #
    #
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/', yarnerprofile, name='yarnerprofile'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follow/', follow_yarner, name='follow_yarner'),
    path('u/<str:username>/unfollow/', unfollow_yarner, name='unfollow_yarner'),


    #
    path("api/add_yarn/", api_add_yarn, name = 'api_add_yarn'),
    path("api/add_like/", api_add_like, name = 'api_add_like'),


    #admin 
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
