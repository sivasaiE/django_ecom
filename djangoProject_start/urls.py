"""
URL configuration for djangoProject_start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from djangoProject_start.views import hello, thankYou, hello_withName, users, user
from djangoProject_start.rest_views import UserList, UserRetrieveDestroyAPIView

urlpatterns = [
    path('thankYou/', thankYou),
    path('hello/', hello),
    path('hello_withName/<name>', hello_withName),
    path('user/', UserList.as_view()),
    path('user/<id>',UserRetrieveDestroyAPIView.as_view() ),
    path('admin/', admin.site.urls),
]
