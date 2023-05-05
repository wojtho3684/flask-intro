"""
This application shows how to redirect user to other page 
and create paths using url_for()
"""
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Template displays the name of the person. The name must be present
# http://localhost:8080/person1/Tom
@app.route('/person1/<i>')
def greeting1(i):
    return render_template('person1.html', fname = i)


# Redirection to the previous page
# http://localhost:8080/person5/Tom
@app.route("/person5/<fname>")
def greeting5(fname):
    return redirect(url_for('greeting1', i = fname))


# Template list_of_links.html displays a list of links to pages
# See http://localhost:8080/links
@app.route("/links")
def links():
    # Empty list
    l = []
    # We add URLs for differenet person
    l.append(url_for('greeting1', i = 'Jane'))
    l.append(url_for('greeting1', i = "John"))
    l.append(url_for('greeting5', fname = "Kate"))
    l.append(url_for('picture1'))
    return render_template('list_of_links.html', list = l)


# Template picture.html displays a static picture
# http://localhost:8080/picture
@app.route("/picture")
def picture1():
    return render_template('picture.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
