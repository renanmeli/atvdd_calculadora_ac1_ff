from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calculadora.html')

@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['operacao']

    if (operacao == "soma" or operacao == "+"):
        resultado = int(valor1) + int(valor2)

    if (operacao == "tira" or operacao == "-"):
        resultado = int(valor1) - int(valor2)

    if (operacao == "multiplica" or operacao == "*"):
        resultado = int(valor1) * int(valor2)

    if (operacao == "divide" or operacao == "/"):
        resultado = int(valor1) / int(valor2)

    return str(resultado)


if __name__ == "__main__":
    app.run(debug=True)