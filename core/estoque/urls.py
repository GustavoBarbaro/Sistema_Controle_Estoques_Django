from django.urls import path


from . import views


urlpatterns = [
    path('movimentacao/', views.criar_movimentacao, name='criar_movimentacao'),
    path('produto/buscar/', views.buscar_produto_por_tag, name='buscar_produto_por_tag'),
    path('usuario/buscar/', views.buscar_usuario_por_tag, name='buscar_usuario_por_tag'),
    path('produto/status/', views.verifica_status, name='verifica_status')
]