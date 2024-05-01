import csv
import psycopg2

conn=psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
    password="Nnaz9191%", port=5432)
cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Phone (
    surname VARCHAR(255),
    name VARCHAR(255),
    number VARCHAR(20)
);
""")
def createpattern():
    print("Do you want to search by surname/name/number or break?(1,2,3,4)")
    mode=input()
    if mode=="1":
        print("Enter surname:")
        b=input()
        print("Is this substring equal/beginning/ending/contained to/of/of/by string?(1,2,3,4)")
        mode=input()
        if mode=='1':
            cur.execute("""SELECT * FROM PHONE WHERE surname=={}""".format(b))
        elif mode =='2':
            cur.execute("""SELECT * FROM PHONE WHERE surname LIKE '{}%'""".format(b))
        elif mode =='3':
            cur.execute("""SELECT * FROM PHONE WHERE surname LIKE '%{}'""".format(b))
        elif mode =='4':
            cur.execute("""SELECT * FROM PHONE WHERE surname LIKE '%{}%'""".format(b))
        print(cur.fetchall())
    elif mode=="2":
        print("Enter name:")
        b=input()
        print("Is this substring equal/beginning/ending/contained to/of/of/by string?(1,2,3,4)")
        mode=input()
        if mode=='1':
            cur.execute("""SELECT * FROM PHONE WHERE name=={}""".format(b))
        elif mode =='2':
            cur.execute("""SELECT * FROM PHONE WHERE name LIKE '{}%'""".format(b))
        elif mode =='3':
            cur.execute("""SELECT * FROM PHONE WHERE name LIKE '%{}'""".format(b))
        elif mode =='4':
            cur.execute("""SELECT * FROM PHONE WHERE name LIKE '%{}%'""".format(b))
        print(cur.fetchall())
    elif mode=="3":
        print("Enter number:")
        b=input()
        print("Is this substring equal/beginning/ending/contained to/of/of/by string?(1,2,3,4)")
        mode=input()
        if mode=='1':
            cur.execute("""SELECT * FROM PHONE WHERE number=={}""".format(b))
        elif mode =='2':
            cur.execute("""SELECT * FROM PHONE WHERE number LIKE '{}%'""".format(b))
        elif mode =='3':
            cur.execute("""SELECT * FROM PHONE WHERE number LIKE '%{}'""".format(b))
        elif mode =='4':
            cur.execute("""SELECT * FROM PHONE WHERE number LIKE '%{}%'""".format(b))
        print(cur.fetchall())
    else:
        return "error"
def delete(var,val):
    cur.execute("""DELETE FROM PHONE WHERE {}='{}'""".format(var,val))
def findname(n):
    cur.execute("""SELECT * FROM PHONE WHERE name='{}'""".format(n))
    a=cur.fetchall()
    if not a:
        return True
    else:
        return False
        

mode = "enter"
while True:
    print("Text \"Enter\" for inserting additional data or \"break\" to stop")
    mode=input()
    if mode=="break":
        break
    table=[]
    print("Enter surname:")
    table.append(input())
    print("Enter name:")
    table.append(input())
    print("Enter number:")
    table.append(input())
    table=tuple(table)
    cur.execute("""INSERT INTO Phone (surname, name, number) VALUES
    {};
    """.format(table))
while True:
    print("Do you want to find something?")
    mode=input()
    if mode=="no":
        break
    createpattern()
while True:
    print("Do you want  to delete something?")
    mode=input()
    if mode=="no":
        break
    print("What do you want to delete?(name or number)")
    var=input()
    cur.execute("""SELECT * FROM Phone""")
    print(cur.fetchall())
    print("Enter value:")
    val=input()
    delete(var,val)
while True:
    print("Do you want to edit the table?")
    mode=input()
    if mode=="no":
        break
    print("Enter name:")
    name=input()
    if findname(name):
        print("Enter surname:")
        sn=input()
        print("Enter phone:")
        p=input()
        cur.execute("""INSERT INTO Phone (surname, name, number) VALUES ('{}','{}','{}')""".format(name,sn,p))
    else: 
        print("Enter new phone number:")
        p=input()
        cur.execute("""UPDATE Phone SET number={} WHERE name='{}'""".format(p,name))
    
conn.commit()
cur.close()
conn.close()