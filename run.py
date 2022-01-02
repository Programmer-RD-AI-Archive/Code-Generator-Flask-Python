from flask import *

app = Flask(__name__)
app.debug = True
app.secret_key = "TEST"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
