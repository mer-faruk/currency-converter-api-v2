from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/convert')
def converter_currency():
    try:
        amount = float(request.args.get('amount'))
        from_currency = request.args.get('from')
        to_currency =request.args.get('to')

        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        converted = data.json['rates'][to_currency]

        return jsonify({
            'amount': amount,
            'from': from_currency,
            'to' : to_currency,
            'converted_amount' : converted

        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

