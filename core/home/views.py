from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from typing import Any
from django.urls import reverse_lazy, reverse


from estoque.models import Movimentacao
from django.db.models import Subquery, OuterRef, Max


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_content = {'today': datetime.today()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now()  # Use datetime.now() para obter a data e hora atuais
        return context
    

class EstoqueView(LoginRequiredMixin, ListView):
    model = Movimentacao
    template_name = 'home/estoque_list.html'
    context_object_name = 'estoque'  # Nome do contexto para o template
    redirect_field_name = 'next' # para redirecionar novamente para essa view apos o login
    login_url = '/login'

    def get_queryset(self):
        # Obtemos o ID da última movimentação para cada produto
        ultima_movimentacao = (
            Movimentacao.objects
            .values('produto')  # Agrupa por produto
            .annotate(ultima_id=Max('id'))  # Obtém a última data
        )

        # Extraímos uma lista de IDs das movimentações mais recentes
        ids_movimentacoes = [
            Movimentacao.objects
            .filter(produto=item['produto'], id=item['ultima_id'])
            .values_list('id', flat=True)[0]
            for item in ultima_movimentacao
        ]

        # Filtra apenas as movimentações do tipo 'Entrada'
        return Movimentacao.objects.filter(
            id__in=ids_movimentacoes, tipo='Entrada'
        ).select_related('produto')


class EstoqueLog(LoginRequiredMixin, ListView):
    model = Movimentacao
    template_name = 'home/estoque_log.html'
    context_object_name = 'movimentacoes'
    redirect_field_name = 'next' # para redirecionar novamente para essa view apos o login
    login_url = '/login'

class loginEstoque(LoginView):
    template_name = 'home/login.html'


class logoutEstoque(LogoutView):
    template_name = 'home/logout.html'


class SignupEstoque(CreateView, LoginRequiredMixin):

    form_class = CustomUserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home')
    # success_url = '/'


    #daria para usar o ligin_url e redirecionar pra outro lugar se fosse o caso de o usuário NÃO estar logado
    #mas como ele está logado: 

    #precisamos dar override no metodo get 
    #para permitir apenas q usuários não logados acessem o signin

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        if self.request.user.is_authenticated:
            return redirect('home')

        return super().get(request, *args, **kwargs)
    
    #isso aqui eh pra salvar o form (mesmo que a create view ja faca isso)
    def form_valid(self, form):
        user = form.save()  # Salva o novo usuário
        # Autentica e faz login do usuário recém-criado
        login(self.request, user)  
        return redirect(self.success_url)  # Redireciona para a home
