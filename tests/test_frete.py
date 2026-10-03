import pytest

# Como a implementação ainda não foi criada, importamos uma função hipotética
# que será criada posteriormente, por exemplo, no módulo 'src.frete'.
try:
    from src.frete import calcular_total
except ImportError:
    # Fallback apenas para os testes não quebrarem imediatamente na ausência do módulo.
    # Remova isso quando a implementação real for criada.
    def calcular_total(subtotal: float) -> float:
        raise NotImplementedError("Implementação pendente")


def test_calculo_frete_padrao():
    """
    Testa se o valor total é calculado adicionando a taxa de frete padrão
    para subtotais abaixo de R$ 200,00.
    """
    # [RB-01] THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho.
    subtotal = 100.00
    esperado = 115.00

    resultado = calcular_total(subtotal)

    assert resultado == esperado


def test_calculo_frete_gratis_limite_exato():
    """
    Testa se o frete é zerado quando o subtotal atinge exatamente R$ 200,00.
    """
    # [RB-02] IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
    subtotal = 200.00
    esperado = 200.00

    resultado = calcular_total(subtotal)

    assert resultado == esperado


def test_calculo_frete_gratis_acima_do_limite():
    """
    Testa se o frete é zerado quando o subtotal ultrapassa R$ 200,00.
    """
    # [RB-02] IF o subtotal do carrinho for maior ou igual a R$ 200,00, THEN THE SYSTEM SHALL conceder frete grátis (taxa = R$ 0,00).
    subtotal = 250.00
    esperado = 250.00

    resultado = calcular_total(subtotal)

    assert resultado == esperado