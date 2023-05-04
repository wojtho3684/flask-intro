from flask import Flask, url_for, redirect, request, make_response, render_template

app = Flask(__name__)

@app.route("/form")
def display_form():
    return render_template("form.html")


# Page /welcome reads data from the form and displays them using template greeting.html
@app.route('/greeting', methods = ['POST','GET'])
def handle_form():

    if request.method == 'POST':
        i = request.form['fname']
        return render_template('greeting.html', fname = i)
    else:
        return redirect(url_for('display_form'))


if __name__ == "__main__":
    app.run(debug=True)
