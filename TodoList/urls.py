"""
URL configuration for TodoList project.

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

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignupView.as_view(),name="signup"),
    path('',views.SignInView.as_view(),name="signin"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('task/add/',views.TaskCreateView.as_view(),name="task-add"),
    path("task/<int:pk>/change/",views.TaskUpdateView.as_view(),name="task-update"),
    path("task/<int:pk>/remove/",views.TaskDeleteView.as_view(),name="task-delete"),
    path('signout/',views.LogoutView.as_view(),name="logout"),
    
    
]
