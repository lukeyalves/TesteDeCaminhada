from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        genero = request.form['genero']
        altura = float(request.form['altura'])
        peso = float(request.form['peso'])
        circuito = float(request.form['circuito'])
        voltas = int(request.form.get('voltas', 0))  # <- ESSA LINHA ESTAVA FALTANDO

        # Distância real percorrida
        distancia_real = voltas * circuito

        # Cálculo da distância ideal
        if genero == 'masculino':
            distancia_ideal = (7.57 * altura) - (5.02 * idade) - (1.76 * peso) - 309
        else:
            distancia_ideal = (2.11 * altura) - (2.29 * peso) - (5.78 * idade) + 667

        # Porcentagem e classificação
        percentual = (distancia_real / distancia_ideal) * 100 if distancia_ideal > 0 else 0

        if percentual > 90:
            classificacao = "Excelente"
        elif percentual > 80:
            classificacao = "Bom"
        elif percentual > 70:
            classificacao = "Regular"
        elif percentual > 60:
            classificacao = "Fraco"
        else:
            classificacao = "Muito fraco / Risco"

        return render_template('resultado.html',
                               nome=nome,
                               distancia_real=round(distancia_real, 2),
                               distancia_ideal=round(distancia_ideal, 2),
                               percentual=round(percentual, 1),
                               classificacao=classificacao)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
