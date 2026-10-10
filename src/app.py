from flask import Flask, request, jsonify
from src.frete import calcular_total

app = Flask(__name__)

@app.route('/checkout/frete', methods=['POST'])
def checkout_frete():
    dados = request.get_json()
    if not dados or 'subtotal' not in dados:
        return jsonify({'erro': 'Subtotal não fornecido'}), 400
    
    try:
        subtotal = float(dados['subtotal'])
        total = calcular_total(subtotal)
        return jsonify({'total': total}), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
