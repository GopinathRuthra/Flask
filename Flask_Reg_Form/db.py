import sqlite3  
  
con = sqlite3.connect("customer.db")  
print("Database opened successfully")  
  
con.execute("create table Registration (id INTEGER PRIMARY KEY AUTOINCREMENT, Customername TEXT NOT NULL, Job TEXT NOT NULL, BName TEXT NOT NULL,tname TEXT NOT NULL,CType TEXT NOT NULL,State TEXT NOT NULL, Tenure TEXT NOT NULL,Goals TEXT NOT NULL,Service TEXT NOT NULL,Product TEXT NOT NULL )")  
  
print("Table created successfully")  
  
con.close()
