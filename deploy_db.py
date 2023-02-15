# CREATING WHOLE SCHEMA ON POSTGRESQL
import psycopg2
from sql_queries import *

def create_database(name):
    
    try:
        conn = psycopg2.connect(database = 'testdb',user = 'postgres',password = 'admin')
    
    except psycopg2.Error() as e:
        print('error while creating the connection\n')
        print(e)

    conn.set_session(autocommit=True)    
    try:
        cur=conn.cursor()
    except psycopg2.Error() as e:
        print("error while creating the cursor\n")
        print(e)
        
    cur.execute(f"DROP DATABASE IF EXISTS {name}")
    conn.commit()
    cur.execute(f"CREATE DATABASE {name}")
    conn.commit()
    cur.close()
    conn.close()
    
    try:
        conn=psycopg2.connect(f"host=localhost dbname={name} user=postgres password=Bas617448")
    except psycopg2.Error() as e:
        print("error while connecting with new database \n")
        print(e)
        
    try:
        cur=conn.cursor()
    except psycopg2.Error() as e:
        print("error while creating the cursor for the new database \n")
        print(e)
    return conn,cur

def create_tables(conn,cur):
    for query in DROP_TABLE_QUERIES:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error() as e:
            print('UNABLE TO DROP TABLE THROUGH THIS QUERY: {}'.format(query))
            print(e)
    for query in CREATE_QUERIES:
        try:
            cur.execute(query)
            conn.commit()
            print(query+'  ...............EXECUTED SUCCESSFULLY')
        except psycopg2.Error() as e:
            print('UNBLE TO CREATE TABLE THROUGH THIS QUERY: {}'.format(query))
            print(e)

def main():
    conn,cur = create_database("sparkifydb")

    create_tables(conn=conn,cur=cur)

    conn.close()

if __name__=="__main__":

    main()
