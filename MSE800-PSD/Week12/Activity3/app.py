from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return render_template("index.html")

@app.route("/bye")
def bye_flask():
    return "<p>Bye, Flask!</p>"

@app.route("/username/<name>")
def learn(name):
    return f"{name} is learning Flask!"

@app.route("/<name>/<int:number>")
def learn_time(name, number):
    return f"{name} is learning Flask! She wakes up at {number} every day"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
