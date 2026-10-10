import pytest
from src.frete import calcular_total
from src.app import app

@pytest.fixture
def cliente_teste():
    """Configura o cliente de testes do Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_integracao_rota_frete(cliente_teste):
    """IT-01: Integração da rota web Flask com a função calcular_total."""
    # Simula requisição HTTP via cliente de teste para a rota de checkout[cite: 1].
    resposta = cliente_teste.post('/checkout/frete', json={'subtotal': 100.00})

    # A interface deve acionar o módulo, formatar e devolver com sucesso[cite: 1, 4].
    assert resposta.status_code == 200
    assert resposta.json['total'] == 115.00