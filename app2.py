from flask import Flask, render_template

app = Flask(__name__)

# Use index.html template
@app.route('/')
def index():
    return render_template('index.html')


# Here the name must be used
@app.route('/greeting1/<i>')
def greeting1(i):
    return render_template('person1.html', fname = i)


# Accepts also empty requests
@app.route('/greeting2/<i>')
def greeting2(i):
    return render_template('person2.html', fname = i)

@app.route("/greeting3")
def greeting3():
    return render_template('person2.html')


# Use Python list to display a list of people
@app.route("/list")
def greeting4():
    l = ["Ben", "Monica", "Ann", "Bob"]
    return render_template('list.html', list = l)


if __name__ == "__main__":
    app.run(debug=True)
