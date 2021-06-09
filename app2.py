from flask import Flask, render_template

app = Flask(__name__)

# Funkcja wyświetlająca stronę przy pomocy szablonu index.html trzymanego w folderze templates/
@app.route('/')
def index():
    return render_template('index.html')


# Funkcja wyświetlająca przywitanie osoby o imieniu podanym w adresie strony. Imię przekazywane jest do szablonu.
@app.route('/osoba/<i>')
def powitanie1(i):
    return render_template('osoba1.html', imie = i)


# J.w. tylko szablon osoba2.html zmienia swoje działanie w zależności od tego czy podano imię, czy nie.
@app.route('/ktos/<i>')
def powitanie2(i):
    return render_template('osoba2.html', imie = i)

@app.route("/ktos")
def powitanie3():
    return render_template('osoba2.html')


# Szablon lista.html wyświetla osoby na liście numerowanej.
@app.route("/lista")
def powitanie4():
    l = ["Maja", "Ola", "Ania", "Andrzej"]
    return render_template('lista.html', lista = l)


if __name__ == "__main__":
    app.run(debug=True)
