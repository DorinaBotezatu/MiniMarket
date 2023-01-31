from flask import Flask, render_template, request, flash
from produse import functii as functii_produse

app = Flask(__name__)
app.secret_key = "abcdef"


@app.route("/")
def index():
    try:
        produse = functii_produse.citeste_produse_mysql()
        return render_template("index1.html", produse=produse)
    except Exception as e:
        print(e)


@app.route("/produs/<id>")
def produs(id):
    produs = functii_produse.citeste_produs_mysql(id)
    return render_template("detalii_produs.html", produs=produs)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
