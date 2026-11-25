
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    varNama = request.form.get("parNama", "").strip()

    if not varNama:
        varNama = "Anonim"

    return f"<h2>Halo, {escape(varNama)}! Selamat datang di Flask First App 🚀</h2>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)

