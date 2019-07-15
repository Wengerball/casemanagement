"""casemanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from cases import views
from django.conf.urls import url,include

urlpatterns = [
    path('', views.redirection),
    url('admin/', admin.site.urls),
    url('login.html/', views.auth_login, name='auth_login'),
    url('view.html/', views.dashboard, name='dashboard'),
    path('addcase/', views.addcase,  name='addcase'),
    path('addtask/<int:id>/', views.addtask, name='addtask'),
    path('viewtask/<int:id>/', views.viewtask, name='viewtask'),
    path('edittask', views.edittask, name='edittask'),
    path('editcase/<int:id>/', views.editcase, name='editcase'),
    path('deletecase/<int:id>/',views.deletecase, name='deletecase'),
    # url(r'^$',views.redirect),
    #path('add/', views.add),
    #path('delete/', views.delete),
    #path('edit', views.edit),
]
