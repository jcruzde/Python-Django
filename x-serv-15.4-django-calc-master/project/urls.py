"""project URL Configuration

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
from calc import views

urlpatterns = [
    path('', views.saludar),
    path('suma/<int:n1>/<int:n2>', views.suma),
    path('resta/<int:n1>/<int:n2>', views.resta),
    path('div/<int:n1>/<int:n2>', views.div),
    path('multi/<int:n1>/<int:n2>', views.multi),
    path('admin/', admin.site.urls),
]