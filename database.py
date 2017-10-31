import sqlite3 as sql

def connectDB:
    conn = sql.connect('users.db')
    c = conn.cursor()

def closeDB:
    conn.commit()
    conn.close()

connectDB()
x = c.execute("SELECT firstname, lastname FROM users.app_users")
print("getUsers")
# userinfo = zip(x[firstname], x[lastname])
closeDB()
'''
# Return all current usernames
def getUsers:
    connectDB()
    x = c.execute("SELECT firstname, lastname FROM users.app_users")
    print("getUsers")
    userinfo = zip(x[firstname], x[lastname])
    closeDB()

# Insert new user information into a db
def insertUser:
    connectDB()
    c.execute("INSERT INTO users.app_users VALUES (?,?,?)", registeruser)
    closeDB()

# Delete current user
def deleteUser:
    connectDB()
    c.execute("DELETE * FROM users.app_users WHERE user_id = (?)", currentuserid)
    c.execute("DELETE * FROM users.user_pw WHERE user_id = (?)", currentuserid)
    closeDB()
'''
