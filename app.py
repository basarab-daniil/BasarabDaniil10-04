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
    scuola = dizionario.get('Scuola', {}).get(0)
    hobby = dizionario.get('Hobby', {}).get(0)
    return render_template('index.html', nome=nome, cognome=cognome, scuola=scuola, hobby=hobby)

@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"],
            "Scuola": request.form["scuola"],
            "Hobby": request.form["hobby"]
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