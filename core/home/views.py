from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, ListView

from estoque.models import Movimentacao
from django.db.models import Subquery, OuterRef, Max


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


class EstoqueLog(ListView):
    model = Movimentacao
    template_name = 'home/estoque_log.html'
    context_object_name = 'movimentacoes'