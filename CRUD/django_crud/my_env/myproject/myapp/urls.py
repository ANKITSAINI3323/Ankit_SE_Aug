"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/',views.add_student,name="add_student"),
    path('all-student/',views.all_student,name="all_student"),
    path('search_student/',views.search_student,name="search_student"),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student'),
    path('update_student/<int:pk>/',views.update_student,name='update_student'),
    path('change_student/',views.change_student,name='change_student'),
]
