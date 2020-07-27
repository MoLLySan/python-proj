"""Planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from planer.views import room_list , Meeting_list, Meeting_room_list, meet_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('room_list/', room_list),
    path('meeting_list/', Meeting_list),
    path('meeting_list/<int:r_id>', Meeting_room_list,name='Meeting_room_list'),
    path("create_meet/", meet_create)
]
