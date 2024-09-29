"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todoapp import views
from django.urls.conf import include

urlpatterns = [
    path('register/',views.register, name='register'),
    path('',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('todo/',views.todo_list,name="todo_list"),
    path('todo/create',views.create_todo,name="create_todo"),
    path('todo/complete/<int:todo_id>',views.complete_todo,name="complete_todo"),
    path('todo/delete/<int:todo_id>',views.delete_todo,name="delete_todo"),
    path('admin/', admin.site.urls),
    path('home/',views.homepage, name='home'),
    

   





    



]

