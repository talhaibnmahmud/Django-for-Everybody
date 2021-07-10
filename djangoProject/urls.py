"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from pathlib import Path

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

# from home.views import MainView
from django.views.static import serve

urlpatterns = [
    # path('ads/', include('ads.urls')),
    # path('autos/', include('autos.urls')),
    # path('cats/', include('cats.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # path('', MainView.as_view()),
    # path('hello/', include('hello.urls')),
]

# Serve the Static HTML
BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns += [
    url(
        r'^site/(?P<path>.*)$',
        serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except PermissionError:
    print('Using registration/login.html as the login template')
