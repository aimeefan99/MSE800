from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", error=None)


@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    weight = float(request.form["weight"])
    height = float(request.form["height"])

    if weight <= 0 or height <= 0:
        return render_template(
            "index.html",
            error="Weight and height must be greater than 0.",
        )

    bmi = weight / (height * height)
    comment = ""

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
        comment = "Consider regular exercise and balanced eating habits.A healthy lifestyle plan may help improve your BMI."

    return redirect(url_for("show_bmi", name=name, bmi=round(bmi, 2), category=category, comment=comment))


@app.route("/username/<name>")
def show_bmi(name):
    bmi = request.args.get("bmi")
    category = request.args.get("category")
    comment = request.args.get("comment")
    return render_template("result.html", name=name, bmi=bmi, category=category, comment=comment)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
