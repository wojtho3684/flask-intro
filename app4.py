from flask import Flask, url_for, redirect, request, make_response, render_template

app = Flask(__name__)

# Szablon formularz.html wyświetla formularz umożliwiający wpisnie imienia i wysłanie go do strony /przywitanie
@app.route("/formularz")
def wyswietl_formularz():
    return render_template("formularz.html")


# Strona /przywitanie odczytuje dane przesłane z formularza i wyświetla je przy pomocy szablonu przywitanie.html.
@app.route('/przywitanie', methods = ['POST','GET'])
def obsluga_formularza():

    if request.method == 'POST':
        i = request.form['imie']
        return render_template('przywitanie.html', imie = i)
    else:
        return redirect(url_for('wyswietl_formularz'))


if __name__ == "__main__":
    app.run(debug=True)
