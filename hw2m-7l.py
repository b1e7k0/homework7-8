import sqlite3

# with sqlite3.connect('students.sqlite3') as con:
#     cur = con.cursor()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS students(
# hobby TEXT ,
# name TEXT ,
# surname TEXT ,
# data_dr DATE ,
# hw_point INT )''')

db = sqlite3.connect('students.sqlite3')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students(
hobby TEXT , 
 name TEXT , 
 surname TEXT , 
 data_dr DATE , 
 hw_point INT 
)''')

c.execute('''INSERT INTO students VALUES ('football', 'Mirlan', 'Aitbaev', '2006-08-10', 10)''')
c.execute('''INSERT INTO students VALUES ('chess', 'Bek', 'Isaev', '2006.08.10', 7)''')
c.execute('''INSERT INTO students VALUES ('basketball', 'Ibragim', 'Ahunbaev', '2006.08.10', 5)''')
c.execute('''INSERT INTO students VALUES ('tenis', 'Alina', 'Isakovna', '2006.08.10', 9)''')
c.execute('''INSERT INTO students VALUES ('gaming', 'Tilek', 'Neymarov', '2006.08.10', 2)''')
c.execute('''INSERT INTO students VALUES ('climbing', 'Bektur', 'Moldogasiev', '2006.08.10', 10)''')
c.execute('''INSERT INTO students VALUES ('football', 'Nurcho', 'Nuraliev', '2006.08.10', 5)''')
c.execute('''INSERT INTO students VALUES ('volleyball', 'Park', 'Jin', '2006.08.10', 4)''')
c.execute('''INSERT INTO students VALUES ('guns', 'Hit', 'Man', '2006.08.10', 10)''')
c.execute('''INSERT INTO students VALUES ('collecting', 'James', 'Gun', '2006.08.10', 7)''')
c.execute('''SELECT name FROM students WHERE surname > 10''')
print(c.fetchall())
c.execute("""UPDATE students SET name == 'genius' WHERE hw_point >= 10""")
print(c.fetchall())
c.execute("""DELETE FROM students WHERE rowid % 2 = 0""")
db.commit()
db.close()