from flask import Flask

app = Flask(__name__)

# Funkcja wyświetlająca przywitanie, po wpisaniu w przeglądarce: http://localhost/
@app.route('/')
def index():
    return '<H1>Witaj!</H1>'


# Funkcja wyświetlająca imię podane w adresie strony np.: http://localhost/osoba/Maria
@app.route('/osoba/<imie>')
def powitanie1(imie):
    return '<H1>Witaj ' + imie + '!</H1>'


# Funkcja wyświetlająca imię i nazwisko podane w adresie
@app.route('/osoba/<imie>/<nazwisko>')
def powitanie2(imie, nazwisko):
    return '<H1>Witaj ' + imie + ' ' + nazwisko + '!</H1>'


# Funkcja wyliczająca kwadrat liczby. Flask wymusza podanie w adresie strony wartości liczbowej
@app.route('/kwadrat/<int:liczba>')
def funkcja1(liczba):
    kwadrat = liczba * liczba
    return f'<H1>Kwadrat z {liczba} wynosi {kwadrat} </H1>'


if __name__ == "__main__":
    app.run(debug=True)
