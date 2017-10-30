from flask import *
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/displayRegister")
def displayRegister():
    return render_template("register.html")


@app.route("/displayHome")
def displayHome():
    return render_template("home.html")


@app.route("/insertRegister")
def insertRegister():
    return


if __name__ == "__main__":
    app.run()
