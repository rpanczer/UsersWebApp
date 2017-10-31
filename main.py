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


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/displayRegister")
def displayRegister():
    return render_template("register.html")



@app.route("/displayHome")
def displayHome():
    userlist = connectdb()
    return render_template("home.html", userlist=userlist)
    closedb(conn)
    


@app.route("/insertRegister")
def insertRegister():
    return


if __name__ == "__main__":
    app.run()
