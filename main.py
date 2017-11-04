from flask import *
import database as db
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/checkCred", methods=["POST"])
def checkCred():
    username = request.form['username_form']
    password = request.form['password_form']
    status = db.checkcreddb(username, password)
    if status == 1:
        return redirect(url_for("displayHome"))
    else:
        return redirect(url_for("main"))

@app.route("/displayRegister")
def displayRegister():
    return render_template("register.html")


@app.route("/displayHome")
def displayHome():
    userlist = db.connectdb()
    return render_template("home.html", userlist=userlist)


@app.route("/insertUser", methods=["POST"])
def insertUser():
    username = request.form['username_form']
    firstname = request.form['firstname_form']
    lastname = request.form['lastname_form']
    password = request.form['password_form']
    db.pushtodb(username, firstname, lastname, password)
    return redirect(url_for("displayHome"))


@app.route("/users", methods=["DELETE"])
def deleteUser():
    username = request.form["username_form"]
    db.deleteUser(username)
    return redirect(url_for("index.html"))



if __name__ == "__main__":
    app.run()
