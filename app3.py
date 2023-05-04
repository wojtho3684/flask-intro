from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Szablon osoba1.html wyświetla przekazane imię osoby
@app.route('/greeting1/<i>')
def greeting1(i):
    return render_template('person1.html', fname = i)


# Redirection to the other page
@app.route("/greeting5/<fname>")
def greeting5(fname):
    return redirect(url_for('greeting1', i = fname))


@app.route("/links")
def links1():
    # Empty list
    l = []
    # We add URLs for differenet person
    l.append(url_for('greeting1', i = 'Jane'))
    l.append(url_for('greeting1', i = "John"))
    l.append(url_for('greeting5', fname = "Kate"))
    l.append(url_for('picture1'))
    return render_template('list_of_links.html', list = l)


@app.route("/picture")
def picture1():
    return render_template('picture.html')


if __name__ == "__main__":
    app.run(debug=True)
