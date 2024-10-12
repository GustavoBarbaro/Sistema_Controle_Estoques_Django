from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Movimentacao, Produto, Usuario  # Importe o modelo da tabela de Movimentação


@csrf_exempt  # Desativa a verificação CSRF para permitir requisições externas
def criar_movimentacao(request):
    if request.method == 'POST':
        try:
            # Converte o corpo da requisição para JSON
            data = json.loads(request.body.decode('utf-8'))

            # Extraia os dados conforme os campos do seu modelo
            produto_id = data.get('produto_id')
            usuario_id = data.get('usuario_id')
            dia = data.get('data')
            tipo = data.get('tipo')  # Por exemplo, entrada ou saída

            #antes de criar a instancia fazer as verificacoes

            #verificar se o produto já foi cadastrado ou baixado
            #consultar a ultima instancia dele, e ver se eh o oposto do que estou mandando
            ultima_movimentacao = Movimentacao.objects.filter(produto_id=produto_id).order_by('-data', '-id').first()

            # Se existe uma movimentação anterior, faça as verificações
            if ultima_movimentacao:
                if ultima_movimentacao.tipo == tipo:
                    if tipo == 'Entrada':
                        return JsonResponse({'error': 'O Produto ja esta no estoque'}, status=400)
                    elif tipo == 'Saida':
                        return JsonResponse({'error': 'O Produto nao esta no estoque'}, status=400)
            else:
                #ok, não existe movimentação anterior, mas verificar se o tipo eh saida. Para não contabilizar primerio uma saida
                if tipo == 'Saida':
                    return JsonResponse({'error' : 'Produto nao esta no estoque'}, status=400)

            # Cria uma nova instância de Movimentação
            movimentacao = Movimentacao(produto_id=produto_id, usuario_id=usuario_id, data=dia, tipo=tipo)
            movimentacao.save()  # Salva no banco de dados

            # Retorna uma resposta de sucesso
            return JsonResponse({'status': 'Movimentação criada com sucesso'}, status=201)
        
        except KeyError as e:
            return JsonResponse({'error': f'Campo {str(e)} faltando'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)



@csrf_exempt
def buscar_produto_por_tag(request):
    if request.method == 'POST':
        try:
            # Decodifica o corpo da requisição (espera JSON)
            data = json.loads(request.body.decode('utf-8'))
            tag_rfid = data.get('tag_rfid')
            
            # Verifica se o campo tag_rfid foi enviado
            if not tag_rfid:
                return JsonResponse({'error': 'Campo tag_rfid nao fornecido'}, status=400)

            # Busca o produto com base na tag RFID
            try:
                produto = Produto.objects.get(tag_rfid=tag_rfid)
                # Retorna o ID do produto
                return JsonResponse({'produto_id': produto.id}, status=200)
            except Produto.DoesNotExist:
                return JsonResponse({'error': 'Produto nao encontrado'}, status=404)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON invalido'}, status=400)
    
    return JsonResponse({'error': 'Metodo nao permitido'}, status=405)



@csrf_exempt
def buscar_usuario_por_tag(request):
    if request.method == 'POST':
        try:
            # Decodifica o corpo da requisição (espera JSON)
            data = json.loads(request.body.decode('utf-8'))
            tag_rfid = data.get('tag_rfid')
            
            # Verifica se o campo tag_rfid foi enviado
            if not tag_rfid:
                return JsonResponse({'error': 'Campo tag_rfid nao fornecido'}, status=400)

            # Busca o produto com base na tag RFID
            try:
                usuario = Usuario.objects.get(tag_rfid=tag_rfid)
                # Retorna o ID do produto
                return JsonResponse({'usuario_id': usuario.id}, status=200)
            except Usuario.DoesNotExist:
                return JsonResponse({'error': 'Usuario nao encontrado'}, status=404)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON invalido'}, status=400)
    
    return JsonResponse({'error': 'Metodo nao permitido'}, status=405)