# Projeto Lambda: Gerador de Saudação Personalizada

Este projeto implementa uma função Lambda simplíssissilima que gera uma saudação personalizada baseada no nome fornecido e na hora atual do dia.

## Sumário

- [Descrição da Função](#descrição-da-função)
- [Entrada Esperada](#entrada-esperada)
- [Saída Esperada](#saída-esperada)
- [Linguagem e Runtime](#linguagem-e-runtime)
- [Dependências Externas](#dependências-externas)
- [Configuração de Variáveis de Ambiente (se houver)](#configuração-de-variáveis-de-ambiente-se-houver)
- [Instruções para Deploy e Execução](#instruções-para-deploy-e-execução)
- [Como Testar](#como-testar)
- [Como Depurar (Debugging)](#como-depurar-debugging)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Considerações de Segurança](#considerações-de-segurança)
- [Otimização de Custos](#otimização-de-custos)

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