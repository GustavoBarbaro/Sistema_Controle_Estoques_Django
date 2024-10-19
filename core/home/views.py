from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, ListView

from estoque.models import Movimentacao
from django.db.models import Subquery, OuterRef


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_content = {'today': datetime.today()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now()  # Use datetime.now() para obter a data e hora atuais
        return context
    

class EstoqueView(ListView):
    model = Movimentacao
    template_name = 'home/estoque_list.html'
    context_object_name = 'estoque'  # Nome do contexto para o template

    def get_queryset(self):
        # Subquery para obter a última movimentação (maior ID) de cada produto
        ultima_movimentacao = (
            Movimentacao.objects
            .filter(produto=OuterRef('pk'))  # Filtra pela chave primária do produto
            .order_by('-id')  # Ordena decrescentemente pelo ID
            .values('tipo')[:1]  # Pega apenas o tipo da última movimentação
        )

        # Filtra os produtos cuja última movimentação foi do tipo 'Entrada'
        produtos_em_estoque = Movimentacao.objects.annotate(
            ultima_tipo=Subquery(ultima_movimentacao)  # Anota o tipo da última movimentação
        ).filter(ultima_tipo='Entrada')  # Filtra apenas os que têm a última movimentação como 'Entrada'

        return produtos_em_estoque


class EstoqueLog(ListView):
    model = Movimentacao
    template_name = 'home/estoque_log.html'
    context_object_name = 'movimentacoes'