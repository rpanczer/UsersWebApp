import sqlite3 as sql

conn = sql.connect('users.db')

c = conn.cursor()

# Return all current usernames
c.execute("SELECT DISTINCT username, firstname + ' ' + lastname as name FROM users.app_users")

username = 'bpanczer'
firstname = 'Bobby'
lastname = 'Panczer'
userinfo =[username, firstname, lastname]

# Insert new user information into a db
c.execute("INSERT INTO users.app_users VALUES (?,?,?)", userinfo)

#
# c.execute()
