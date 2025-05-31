import json
import datetime

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        nome = body.get('nome', 'Visitante')
    except Exception as e:
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
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
