"""
    URL Configuration

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
# CALLING URL NAME AND THE FUNCTION IN views.py

from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Page Renderers
    path('',views.index,name='index'),

    # APIs
    path('api/getAllDistricts',views.getAllDistricts,name='getAllDistricts')
]

urlpatterns += staticfiles_urlpatterns()
