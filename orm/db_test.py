import sqlite3
conn = sqlite3.connect('test.db')

# cur 为游标对象
cur = conn.cursor()

cur.execute("CREATE TABLE demo(num int, str varchar(20));")
cur.execute("INSERT INTO demo VALUES (%d, '%s')" % (1, 'aaa'))
cur.execute("INSERT INTO demo VALUES (%d, '%s')" % (2, 'bbb'))

cur.execute("UPDATE demo SET str='%s' WHERE num = %d" % ('ddd', 2))

cur.execute("SELECT * FROM demo;")
rows = cur.fetchall()
print("nums of records: ", len(rows))

for _ in rows:
    print(_)

conn.commit()

cur.close()

conn.close()