from flask import Flask, render_template, redirect, url_for, request
import pandas as pd

# inizializza l'app Flask
app = Flask(__name__)

# rotta principale
@app.route('/')
def home():
    df = pd.read_csv("profilo.csv")
    dizionario = df.to_dict()
    nome = dizionario.get('Nome', {}).get(0)
    cognome = dizionario.get('Cognome', {}).get(0)
    return render_template('index.html', nome=nome, cognome=cognome)

@app.route("/inserisci", methods=["GET", "POST"])
def inserisci():
    if request.method == "POST":
        nome = request.form["nome"]
        return f"Hai inserito: {nome}"
    return render_template("form.html")

@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"]
        }
        df = pd.DataFrame([nuovo_profilo])
        df.to_csv("profilo.csv", index=False)
        return redirect(url_for('home'))
    
    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("modifica.html", dati=dati)

# avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)