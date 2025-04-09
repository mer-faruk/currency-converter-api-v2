from flask import Flask, render_template, request 
import requests


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    currencies = []

    response = requests.get("https://api.frankfurter.app/currencies")
    if response.status_code == 200:
        data = response.json()
        currencies = list(data.keys()) 
        
    if request.method == "POST":

        amount = request.form.get("amount")
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")


        if amount and from_currency and to_currency:

            try:
                url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
       
       
                response = requests.get(url)
       
                data = response.json()
        
                result = f"{amount} {from_currency} = {data['rates'][to_currency]} {to_currency}"

            except:
    
                result = "Bir hata oluştu. Lütfen tekrar deneyin."
  
    return render_template("index.html", currencies=currencies, result=result)

if __name__ == "__main__":
    app.run(debug=True)
