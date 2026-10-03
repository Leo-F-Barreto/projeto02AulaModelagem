# File: docs/specs/checkout_frete.md

## Requisitos Funcionais
* **RF-01 (Event-Driven):** WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete.
* **RF-02 (Ubiquitous):** THE SYSTEM SHALL responder 90% resquisições em menos de 2s.
* **RF-03 (Event-Driven):** WHEN o usuário aplicar o cupom 'PROMO10', THE SYSTEM SHALL aplicar 10% sobre o valor total do carrinho.

## Regras de Negócio e Exceções
* **RB-01 (Ubiquitous)**: THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
* **RB-02 (Unwanted Behavior)**: IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
* **RB-03 (Unwanted Behavior):** IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'.