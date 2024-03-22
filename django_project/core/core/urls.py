"""
URL configuration for core project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import home, next_page, contact, about, services
from Vegan.views import Recepies, Delete_recipe, Update_recepie, login_page, register

urlpatterns = [
    path('', login_page,  name = "login_page"),
    path('login_page', login_page,  name = "login_page"),
    path('contact', contact, name = "contact"),
    path('about', about, name = "about"),
    path('services', services, name = "services"),
    path('Recepies', Recepies, name = "Recepies"),
    path('delete-recepies/<id>', Delete_recipe, name = "Delete_recipe"),
    path('update-recepies/<id>', Update_recepie, name = "Update_recepie"),
    path('register', register,  name = "register"),
    
    path('next_page',next_page),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns() 
