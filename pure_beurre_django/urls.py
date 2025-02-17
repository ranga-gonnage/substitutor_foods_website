"""pure_beurre_django URL Configuration

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
from substitutor import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

handler404 = 'substitutor.auxilliaries.home.my_custom_page_not_found_view'

urlpatterns = [
    path("admin/", views.redirect_home),
    url(
        "substitutor/",
        include(
            ("substitutor.urls", "substitutor_namespace"),
            namespace="substitutor_namespace",
        ),
    ),
    path("", views.redirect_home),
]
