from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

@app.route("/")
def hello_flask():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    image = request.files["image"]
    filename = image.filename
    image.save(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    image_url = f"/static/uploads/{filename}"
    return render_template("show_image.html", image_url=image_url, filename=filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
