from django.urls import path


from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('estoque/', views.EstoqueView.as_view(), name='home.estoque'),
    path('estoque/log', views.EstoqueLog.as_view(), name='home.LogEstoque'),
]