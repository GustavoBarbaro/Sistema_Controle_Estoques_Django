"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movimentacao/', views.criar_movimentacao, name='criar_movimentacao'),
    path('api/produto/buscar/', views.buscar_produto_por_tag, name='buscar_produto_por_tag'),
    path('api/usuario/buscar/', views.buscar_usuario_por_tag, name='buscar_usuario_por_tag'),
    path('api/produto/status/', views.verifica_status, name='verifica_status'),
]
