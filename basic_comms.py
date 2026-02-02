import os
import sqlite3 as sql
import random as r


db_path = os.path.join(os.path.dirname(__file__), 'database.db')
conn = sql.connect(db_path)

cursor=conn.cursor()

sql_file_path = os.path.join(os.path.dirname(__file__), 'comms.sql')
with open(sql_file_path, "r") as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()

def check_vat(vat): # + find ID
    vat_lookup = cursor.execute(
        "SELECT client_id FROM clients WHERE vat = ?",(vat,)
    )
    res = vat_lookup.fetchone()
    return res

def fetch_account_balance(ban): #+Check stautus
    ban_lookup = cursor.execute(
        "SELECT balance FROM accounts WHERE ban = ?",(ban,)
    )
    res = ban_lookup.fetchone()
    if res:
        return res
    else:
        return False

def create_customer(name,dob,phoneno,email,homeaddr,vat,citizenof,idnum):
    if check_vat(vat) == False:
        new_cust = cursor.execute(
            "INSERT INTO clients (name,dob,phoneno,email,homeaddr,vat,citizenof,idnum) VALUES(?,?,?,?,?,?,?,?)",(name,dob,phoneno,email,homeaddr,vat,citizenof,idnum)
        )
        customer_id=cursor.lastrowid
        conn.commit()
        return customer_id,True
    else:
        return 'Client is already in database',False

def open_account(vat):
    client_res = check_vat(vat) 
    
    if client_res: 
        client_id = client_res[0] 
        
        new_ban = r.randint(100000, 999999)
        while fetch_account_balance(new_ban):
            new_ban = r.randint(100000, 999999)
            
 
        cursor.execute(
            "INSERT INTO accounts (ban, owner_id, balance) VALUES (?, ?, ?)",
            (new_ban, client_id, 0.00)
        )
        conn.commit()
        return new_ban
    else:
        return False


