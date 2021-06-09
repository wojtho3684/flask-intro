from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Szablon osoba1.html wyświetla przekazane imię osoby
@app.route('/osoba/<i>')
def powitanie1(i):
    return render_template('osoba1.html', imie = i)


# Strona o adresie http://localhost/innaosoba przekierowuje przeglądarkę do powyższego adresu
@app.route("/innaosoba/<imie>")
def powitanie2(imie):
    return redirect(url_for('powitanie1', i = imie))


# Szablon wyświelta przekazaną listę stron w postali listy oraz w postaci odnośników umożliwiających przechodzenie na inne strony aplikacji.
@app.route("/linki")
def linki1():
    # Pusta lista
    l = []
    # Dopisujemy do listy wyniki kolejnych wywołań funkcji url_for
    l.append(url_for('powitanie1', i = 'Ula'))
    l.append(url_for('powitanie1', i = "Marek"))
    l.append(url_for('powitanie2', imie = "Kasia"))
    l.append(url_for('powitanie4'))
    l.append(url_for('obrazek1'))
    return render_template('lista_linkow.html', lista = l)


# Szablon obrazek.html wyświetla statyczny obrazek i używa arkusza stylów zdefiniowanych w folderze static/
@app.route("/obrazek")
def obrazek1():
    return render_template('obrazek.html')


if __name__ == "__main__":
    app.run(debug=True)
