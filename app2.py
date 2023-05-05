"""
This app shows how to use Flask HTML templates
"""
from flask import Flask, render_template

app = Flask(__name__)

# Use index.html template
@app.route('/')
def index():
    return render_template('index.html')


# Template displays the name of the person. The name must be present
# http://localhost:8080/person1/Tom
@app.route('/person1/<i>')
def greeting1(i):
    return render_template('person1.html', fname = i)


# Template person2.html works like the previous one, but...
# http://localhost:8080/person2/Mike
@app.route('/person2/<i>')
def greeting2(i):
    return render_template('person2.html', fname = i)

# it can also accept no argument (it is not possible with person1.html template)
# http://localhost:8080/person3
@app.route("/person3")
def greeting3():
    return render_template('person2.html')


# Template list.html displays an unnumbered list using list passed from Python
# http://localhost:8080/list
@app.route("/list")
def greeting4():
    users = ["Ben", "Monica", "Ann", "Bob"]
    return render_template('list.html', list = users)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
