import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('db.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    cursorObj = con.cursor()
 
    #cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    cursorObj.execute("CREATE TABLE if not exists employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
 
    con.commit()

def insert(con):

	cursorObj = con.cursor()

	cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
 
	con.commit()

def insert_entities(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()

def update_name(con, nombre):
 
    cursorObj = con.cursor()
 
    cursorObj.execute(f'UPDATE employees SET name = "{nombre}" where id = 2')
 
    con.commit()

def select(con):
    
    cursorObj = con.cursor()
 
    cursorObj.execute('Select * from employees')
 
    rows = cursorObj.fetchall()

    print(f"Hay {len(rows)} resultados en la consulta")
    for row in rows:
    	print(row)

def delete(con):
    
    cursorObj = con.cursor()
 
    print(f"Se borraron {cursorObj.execute('delete from employees').rowcount} Registros")

    con.commit()

def sqlite_master(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())

def drop_table(con):

	cursorObj = con.cursor()

	cursorObj.execute('drop table if exists projects')

	con.commit()

con = sql_connection()
 
#sql_table(con)
#insert(con)

#entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
#insert_entities(con, entities)

#nombre = "Andres"
#update_name(con, nombre)

#select(con)

#delete(con)

#sqlite_master(con)

drop_table(con)

con.close()






















