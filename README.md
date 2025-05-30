# Projeto Lambda: Gerador de Saudação Personalizada

Este projeto implementa uma função Lambda simplíssima que gera uma saudação personalizada baseada no nome fornecido e na hora atual do dia.

## Sumário

- [Descrição da Função](#descrição-da-função)
- [Entrada Esperada](#entrada-esperada)
- [Saída Esperada](#saída-esperada)
- [Linguagem-e-Runtime](#linguagem-e-runtime)
- [Como Testar](#como-testar)

---

## Descrição da Função

A função tem como objetivo receber um nome como entrada e retornar uma mensagem de saudação apropriada para o período do dia (Bom dia, Boa tarde, Boa noite) juntamente com o nome fornecido. Se nenhum nome for fornecido, utiliza "Visitante" como padrão.

---

## Entrada Esperada

A função espera um objeto JSON como entrada. O campo principal é `nome`.

**Exemplo de payload de entrada:**

```json
{
  "nome": "Steve Magal"
}
```

---

## Saída Esperada

A função retorna um objeto JSON contendo a saudação e o horário do processamento. Se integrada com o API Gateway, o formato inclui `statusCode` e `body` (como uma string JSON).

**Exemplo de payload de saída (se chamada diretamente ou com teste no console Lambda):**

```json
{
  "statusCode": 200,
  "body": "{\"saudacao\": \"Boa tarde, Maria Silva!\", \"horario_processamento\": \"2025-05-30 14:30:00.123456\"}"
}
```

O `body` é uma string JSON que, ao ser parseada, resulta em:

```json
{
  "saudacao": "Boa tarde, Maria Silva!",
  "horario_processamento": "2025-05-30 14:30:00.123456"
}
```

---

## Linguagem e Runtime

- **Linguagem:** Python  
- **Runtime AWS Lambda:** `python3.9` (ou a versão que você usou)

---

## Como Testar

Console AWS Lambda:

1. Na página da sua função Lambda, vá para a aba **"Test"**.
2. Crie um evento de teste (conforme descrito em Entrada Esperada).

**Exemplo de evento `testComNome`:**

```json
{
  "nome": "Carlos"
}
```

**Exemplo de evento `testSemNome`:**

```json
{}
```

3. Clique em **"Test"**. A saída, resumo e logs serão exibidos.

---

### AWS CLI (Linha de Comando):

```bash
aws lambda invoke \
    --function-name minhaFuncaoSaudacao \
    --payload '{"nome": "Ana via CLI"}' \
    output.json

cat output.json # Para ver a resposta
```

 Substitua `minhaFuncaoSaudacao` pelo nome real da sua função.
