import csv
import psycopg2 

conn=psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
    password="Nnaz9191%", port=5432)
cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number VARCHAR(20)
);
""")

def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cur.execute("""DELETE FROM Phonebook
    WHERE surname='{}'
    """.format(sn))

#FOR INSERTING DATA

mode="enter"
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
    cur.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(table))

while True:
    print("Want to insert data from csv file? (Yes or No)")
    mode=input()
    if mode=="no" or mode=="No":
        break
    print("Enter the name of the file")
    mode=input()
    with open(mode+'.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)",row)

#FOR UPDATING DATA
while True:
    print("Text 'Update' to update something or 'break' to stop")
    mode=input()
    if mode=="break":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtochange=input()
    print("What you want to change? (name or number)")
    mode=input()
    print("Enter new (name or number)")
    newvalue=input()
    update(idtochange, mode, newvalue)

#FOR DELETING DATA
while True:
    print("Do you want to delete some data? (yes or no)")
    mode=input()
    if mode=="no" or mode== "No":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname:")
    idtodelete=input()
    delete(idtodelete)


conn.commit()
cur.close()
conn.close()