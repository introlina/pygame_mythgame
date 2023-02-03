import sqlite3

db = sqlite3.connect('HelpF_Data.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)""")

db.commit()
for i in sql.execute("SELECT login FROM users"):
    print(i)
user_login = input('L: ')
user_password = input('P: ')
if (user_login,) not in sql.execute("SELECT login FROM users"):
    sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
    db.commit()
else:
    print('Такая запись уже имеется')
