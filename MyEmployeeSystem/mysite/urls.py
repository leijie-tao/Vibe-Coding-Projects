"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app01 import views  # <--- 1. 导入 app01 的视图模块

urlpatterns = [
    # path('admin/', admin.site.urls), # 自带的后台先不管
    path('', views.depart_list),

    # 2. 添加这条路由
    # 意思是：访问 /depart/list/ 时，执行 views.py 里的 depart_list 函数
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),
    path('login/', views.login),
    path('logout/', views.logout),
    path('chart/list/', views.chart_list),
    path('chart/bar/', views.chart_bar),
    path('chart/pie/', views.chart_pie),
    path('chart/line/', views.chart_line)
]