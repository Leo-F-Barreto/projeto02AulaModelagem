def calcular_total(subtotal: float) -> float:
    # [RB-03] IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")

    # [RB-02] Se o subtotal do carrinho for maior ou igual a R$ 250,00, conceder frete grátis
    if subtotal >= 250.00:
        taxa_frete = 0.00
    else:
        # [RB-01] Calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal
        taxa_frete = 15.00
        
    return subtotal + taxa_frete
