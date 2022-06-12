from pathlib import Path
import sqlite3
import os
BASE_DIR=BASE_DIR=Path(__file__).resolve().parent.parent
conn=sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
cur=conn.cursor()
sName=input("Name: ")
sSex=input("Sex: ")
sEmail=input("Email: ")
sPhone=input("Phone: ")
sAddr=input("Addr: ")
sql_str="insert into sampleApp_sample(SName,SSex,SEmail,SPhone,SAddr) values('{}','{}','{}','{}','{}');".format(sName,sSex,sEmail,sPhone,sAddr)
conn.execute(sql_str)

conn.commit()