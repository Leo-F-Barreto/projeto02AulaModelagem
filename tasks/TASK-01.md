# TASK-01: Implementação de Cálculo de Frete Padrão e Frete Grátis

## 1. Objetivo
Implementar a lógica de cálculo do valor total do carrinho focando exclusivamente na adição da taxa de frete padrão e na validação da regra de isenção de frete por valor de subtotal.

## 2. Escopo e Restrições (Tamanho Mínimo)
* **O QUE FAZER:** Implementar apenas o cálculo de frete padrão e a regra de frete grátis baseada no valor da compra.
* **O QUE NÃO FAZER:** Não implementar regras de cupons promocionais, exceções de valor negativo ou limites regionais nesta task. 
* **ISOLAMENTO:** Utilize apenas este documento, o arquivo de especificações (`docs/specs/checkout_frete.md`) e a constituição do projeto. O escopo do projeto inteiro não deve ser considerado.

## 3. Requisitos a serem implementados
As seguintes regras de negócio da especificação devem ser atendidas:

* **RB-01:** O sistema deve calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
* **RB-02:** Se o subtotal do carrinho for maior ou igual a R$ 200,00, o sistema deve conceder frete grátis (taxa = R$ 0,00).

## 4. Diretrizes de Rastreabilidade (IMPORTANTE)
O código fonte gerado **deve, obrigatoriamente, referenciar de forma explícita** as cláusulas da especificação através de comentários no código. 

**Exemplo de expectativa no código gerado:**
- Ao definir ou somar os R$ 15,00, incluir comentário referenciando `[RB-01]`.
- Na condicional (if) que verifica se o subtotal é `>= 200.00`, incluir comentário referenciando `[RB-02]`.

## 5. Critérios de Aceite
- [ ] O código calcula corretamente o valor total para subtotais abaixo de R$ 200,00 (somando R$ 15,00).
- [ ] O código calcula corretamente o valor total para subtotais iguais ou superiores a R$ 200,00 (somando R$ 0,00 de frete).
- [ ] O código gerado contém rastreabilidade exata apontando para as cláusulas `RB-01` e `RB-02`.