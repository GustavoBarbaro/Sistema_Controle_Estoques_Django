from django.urls import path


from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('estoque/', views.EstoqueView.as_view(), name='home.estoque'),
    path('estoque/log', views.EstoqueLog.as_view(), name='home.LogEstoque'),
    path('login', views.loginEstoque.as_view(), name='home.login'),
    path('logout', views.logoutEstoque.as_view(), name='home.logout'),
    path('signup', views.SignupEstoque.as_view(), name='home.signup'),
]