"""
This file demonstrates how to use forms to pass arguments from form into app
"""
from flask import Flask, url_for, redirect, request, make_response, render_template

app = Flask(__name__)

# Template form.html displays form to enter a user name
# When you click Send you are redirected to page /greeting
# See: http://localhost:8080/form
@app.route("/form")
def display_form():
    return render_template("form.html")


# Page /greeting reads data from the form and displays them using template greeting.html
# Data from the form is send using POST request
# If you want to open http://localhost:8080/greeting you are redirected to the form
@app.route('/greeting', methods = ['POST','GET'])
def handle_form():

    if request.method == 'POST':
        i = request.form['fname']
        return render_template('greeting.html', fname = i)
    else:
        return redirect(url_for('display_form'))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
