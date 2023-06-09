"""DjangoPro URL Configuration

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
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('cookie',cookie_session_management),
    path('login/',login),
    path('outview/',outview),
    path('student/',get_data),
    path('outview/info/<int:_id>/',info),
    path('outmaster/',outmaster),
    path('outmaster/infomaster/<int:_id>',infomaster),
    path('practice/',practice,name='basic'),
    path('studentdata/',display_data),
    path('student_panel/',student_panel,name="student_panel"),
    path('insert_data/',insert_data,name="insertdata"),
    path('update_data/<int:id>',update_data,name="updatedata"),
    path('delete_data/<int:id>',delete_data,name='deletedata'),
    
    


]
