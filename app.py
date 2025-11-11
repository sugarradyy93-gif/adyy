from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/bidirectional')
def bidirectional():
    return render_template('bidirectional.html')

@app.route('/saham')
def saham():
    return render_template('saham.html')

@app.route('/api/calculator', methods=['POST'])
def api_calculator():
    data = request.get_json()
    a = bool(int(data['a']))
    b = bool(int(data['b']))
    op = data['operator']
    if op == 'AND':
        result = a and b
    elif op == 'OR':
        result = a or b
    elif op == 'XOR':
        result = a != b
    else:
        result = None
    return jsonify({'result': str(result)})

@app.route('/api/predict-word', methods=['POST'])
def predict_word():
    text = request.get_json().get('text', '')
    prediction = text + random.choice([' hebat', ' keren', ' luar biasa'])
    return jsonify({'prediction': prediction})

@app.route('/api/predict-stock', methods=['POST'])
def predict_stock():
    symbol = request.get_json().get('symbol', 'AAPL')
    price = round(random.uniform(100, 500), 2)
    return jsonify({'symbol': symbol, 'predicted_price': price})

if __name__ == '__main__':
    app.run(debug=True)
