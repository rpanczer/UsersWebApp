from flask import *
import sqlite3 as sql
app = Flask(__name__)


def connectdb():
    conn = sql.connect('users.db')
    c = conn.cursor()
    qry = "SELECT firstname, lastname FROM app_users"
    c.execute(qry)
    userlist = c.fetchall()
    return userlist


def closedb(conn):
    conn.commit()
    conn.close()


def inserttodb(username, firstname, lastname, password):
    try:
       conn = sql.connect('users.db')
       c = conn.cursor()
    except Error as e:
        print(e)

    userinfo = (username, firstname, lastname)
    pwinfo = (username, password)
    c.execute("INSERT INTO app_users VALUES(?,?,?)", userinfo)
    c.execute("INSERT INTO user_pws VALUES(?, ?)", pwinfo)
    conn.commit()


def checkcreddb(username, password):
    try:
       conn = sql.connect('users.db')
       c = conn.cursor()
    except Error as e:
        print(e)
    c.execute("SELECT password FROM user_pws WHERE username = (?)", (username,))
    passworddb = c.fetchone()
    if passworddb is not None:
        passworddb = passworddb[0]
        if password == passworddb:
            return 1
    else:
        return 0


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/checkCred", methods=["POST"])
def checkCred():
    username = request.form['username_form']
    password = request.form['password_form']
    status = checkcreddb(username, password)
    print(status)
    if status == 1:
        return redirect(url_for("displayHome"))
    else:
        return redirect(url_for("main"))

@app.route("/displayRegister")
def displayRegister():
    return render_template("register.html")


@app.route("/displayHome")
def displayHome():
    userlist = connectdb()
    return render_template("home.html", userlist=userlist)


@app.route("/insertUser", methods=["POST"])
def insertUser():
    username = request.form['username_form']
    firstname = request.form['firstname_form']
    lastname = request.form['lastname_form']
    password = request.form['password_form']
    inserttodb(username, firstname, lastname, password)
    return redirect(url_for("displayHome"))


if __name__ == "__main__":
    app.run()
