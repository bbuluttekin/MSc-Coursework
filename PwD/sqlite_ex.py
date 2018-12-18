import sqlite3

conn = sqlite3.connect('mydb')

cursor = conn.cursor()

print('Q1: DROP TABLE IF EXISTS')
cursor.execute('DROP TABLE IF EXISTS users')

print('Q2: CREATE TABLE WITH COLUMNS AND DATA TYPES')
cursor.execute(
    'CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, email TEXT unique, password TEXT, city TEXT, salary INTEGER)')

names = ['Stelios', 'Mary', 'John', 'Andrew', 'George', 'Stefan']
phones = ['37288', '34992', '49228', '32991', '34643', '39911']
emails = ['ste@dcs.com', 'mary@dcs.com', 'john@bbk.ac.uk',
          'and@bbk.com', 'geo@bbk.com', 'stef@bbk.com']
passwords = ['1234', '4122', '2455', '4632', '5995', '9911']
cities = ['London', 'London', 'Paris', 'Paris', 'London', 'London']
salary = ['100', '120', '140', '175', '200', '220']

print('Q3: INSERT DATA FROM LISTS')
for i in range(len(names)):
    cursor.execute('''INSERT INTO users(name, phone, email, password, city, salary)
                      VALUES(?,?,?,?,?,?)''', (names[i], phones[i], emails[i], passwords[i], cities[i], salary[i]))

print("Q4: ---- SELECT ALL (*) ----")
# Select all data
cursor.execute('''SELECT * FROM users''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print(' ')
print("Q5: ---- SELECT name, email, phone ----")
# Select all data
cursor.execute('''SELECT name, email, phone FROM users''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print(' ')
print("Q6: ---- SELECT name, email, phone WHERE name is stelios ----")
user_name = 'Stelios'
cursor.execute(
    '''SELECT name, email, phone FROM users WHERE name=?''', (user_name,))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print(' ')
print("Q7: ---- UPDATE USER BY USER ID ----")
# UPDATE PHONE NUMBER OF USER 1
newphone = '55555'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
               (newphone, userid))

user_id = '1'
cursor.execute(
    '''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

# Delete User (id)
print(' ')
print('Q8: ---- DELETE USER ID =1 ----')
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
# Select all to see results
cursor.execute('''SELECT * FROM users''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


print(' ')
print('Q9: ----SELECT USERS WITH PHONE STARTING WITH 3----')
cursor.execute('''SELECT * FROM users WHERE phone LIKE ? ''', ('3%',))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print(' ')
print('Q10: ----SELECT USERS WITH PHONE STARTING WITH 3 AND NAME IS STEFAN----')
cursor.execute(
    '''SELECT * FROM users WHERE phone LIKE ? AND NAME =?''', ('3%', "Stefan"))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print(' ')
print('Q11: ----SELECT USERS WITH EMAIL ENDING bbk.com----')
cursor.execute('''SELECT * FROM users WHERE email LIKE ? ''', ('%bbk.com',))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print(' ')
print('Q12: ----SELECT USERS WITH EMAIL FROM BBK ORDER BY NAME----')
cursor.execute(
    '''SELECT * FROM users WHERE email LIKE ? ORDER BY name''', ('%bbk%',))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}, {5}, {6}'.format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


print(' ')
print('Q13: ---- COUNT HOW MANY USERS LIVE PER CITY ----')
cursor.execute('''SELECT city,COUNT(city) FROM users GROUP BY city''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}'.format(row[0], row[1]))

print(' ')
print('Q14: ---- COUNT HOW MANY USERS LIVE PER CITY AND SHOW THE SUM OF THE SALARY----')
cursor.execute(
    '''SELECT city, SUM(salary), COUNT(city) FROM users GROUP BY city ''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print(' ')
print('Q15: ---- SHOW THE SUM OF THE SALARIES PER CITY FOR CITIES HAVING SUM GREATER THAN 350----')
cursor.execute(
    '''SELECT city, SUM(salary) as mysum FROM users GROUP BY city HAVING mysum >? ''', (350,))
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}'.format(row[0], row[1]))


print(' ')
print("Q16: ---- SELECT name, email, phone WHERE SALARY BETWEEN 100,150 ----")

cursor.execute(
    '''SELECT name, email, phone FROM users WHERE salary BETWEEN ? AND ?''', ('100', '150',),)
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print(' ')
print("Q17: ---- SELECT city, MAX(salary), MIN(salary),AVG(salary), SUM(salary) FROM users GROUP BY city ----")

cursor.execute(
    '''SELECT city, MAX(salary), MIN(salary), SUM(salary), AVG(salary) FROM users GROUP BY city''')
all_rows = cursor.fetchall()

for row in all_rows:
    print('{0} : {1}, {2}, {3}, {4}'.format(
        row[0], row[1], row[2], row[3], round(row[4], 2)))

conn.commit()
conn.close()
