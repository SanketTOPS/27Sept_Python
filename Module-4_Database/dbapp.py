import sqlite3

try:
    dbcon=sqlite3.connect('mydb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Create Table
create_tbl="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,city) values('sanket','rajkot'),('mitesh','surat'),('nirav','baroda'),('ashok','bhavnagar'),('meet','rajkot'),('harsh','ahmedabad')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set city='junagadh' where id=5"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=6"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


cur=dbcon.cursor()

# Select Data
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)
    for i in data:
        print(i[2])
except Exception as e:
    print(e)
