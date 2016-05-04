
"""My flask app"""

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/submit", methods=['POST'])
def submit():
    messages.append(request.form['message'])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)