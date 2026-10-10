import pytest
from src.frete import calcular_total

def test_bloqueio_carrinho_invalido():
    """FT-01: Bloqueio e exibição de erro para valores de carrinho inválidos."""
    # Carrinhos zerados ou negativos devem abortar o cálculo e levantar erro.
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_total(0.00)

    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_total(-10.00)