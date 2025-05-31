import json
import datetime

def lambda_handler(event, context):
    try:
        nome = event.get('nome', 'Visitante') 
    except AttributeError:
        nome = 'Visitante (entrada inválida)'

    agora = datetime.datetime.now()
    hora = agora.hour

    if 5 <= hora < 12:
        periodo = "Bom dia"
    elif 12 <= hora < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"

    mensagem_saudacao = f"{periodo}, {nome}!"

    print(f"Requisição recebida para: {nome}")
    print(f"Saudação gerada: {mensagem_saudacao}")

    return {
        'statusCode': 200, 
        'body': json.dumps({
            'saudacao': mensagem_saudacao,
            'horario_processamento': str(agora)
        })
    }

#teste de função lambda
# if __name__ == '__main__':

#     evento_teste_com_nome = {'nome': 'Aluno'}
#     evento_teste_sem_nome = {}
#     evento_teste_invalido = "Teste"

#     print("--- Teste com nome ---")
#     print(lambda_handler(evento_teste_com_nome, None))
#     print("\n--- Teste sem nome ---")
#     print(lambda_handler(evento_teste_sem_nome, None))
#     print("\n--- Teste com entrada inválida ---")
#     print(lambda_handler(evento_teste_invalido, None))