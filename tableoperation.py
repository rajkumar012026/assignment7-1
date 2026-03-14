import psycopg2
import pandas as pd
def getConnection():
    try:
        conn = psycopg2.connect(dbname="testdb", user="amar", password="123456789", host="localhost",
                                port="5432")
        cursor = conn.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    else:
        print("Connected to PostgreSQL successfully")
def create_table():
    conn = psycopg2.connect(dbname="testdb", user="postgres", password="795472", host="localhost",
                            port="5432")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE employee(id int, name text, age int)")
    conn.commit()
    conn.close()
    print("Table created successfully")
def insert_data():
    print("Enter data to insert to the table employee")
    input_id = int(input("Enter employee id: "))
    input_name = input("Enter employee name: ")
    input_age = int(input("Enter employee age: "))
    try:
       conn = psycopg2.connect(dbname="testdb", user="postgres", password="795472", host="localhost",
                                    port="5432")
    except psycopg2.Error as e:
            print(e)
    else:
       cursor = conn.cursor()
       sql_insert = "insert into employee (id, name, age) values (%s, %s, %s);"
       cursor.execute(sql_insert, (input_id, input_name, input_age))
       conn.commit()
       cursor.close()
       print("The data inserted successfully")
def delete_data():
    '''
    The function deletes the data from the table employee with the given id
    :return:
    '''
    input_id = int(input("Enter id of the employee which you want to delete: "))

    try:
        conn = psycopg2.connect(dbname="testdb", user="postgres", password="795472", host="localhost",
                                port="5432")
    except psycopg2.Error as e:
        print(e)
    else:
        cursor = conn.cursor()
        sql_delete = "delete from employee where id = %s;"
        cursor.execute(sql_delete, (input_id,))
        conn.commit()
        cursor.close()
        print("The data deleted successfully")
def update_data():
    '''
    The function updates the data associated with name of the employee with the given id
    :return:
    '''
    input_id = int(input("Enter id of the employee which you want to delete: "))
    input_newname = input("Enter new employee name: ")

    try:
        conn = psycopg2.connect(dbname="testdb", user="postgres", password="795472", host="localhost",
                                port="5432")
    except psycopg2.Error as e:
        print(e)
    else:
        cursor = conn.cursor()
        sql_delete = "update employee set name = %s where id = %s;"
        cursor.execute(sql_delete, (input_newname,input_id,))
        conn.commit()
        cursor.close()
        print("The data updated successfully")
def view_data():
    '''
        The function show the data associated with the employee id
        :return:
        '''
    #input_id = int(input("Enter id of the employee which you want to delete: "))


    try:
        conn = psycopg2.connect(dbname="testdb", user="postgres", password="795472", host="localhost",
                                port="5432")
    except psycopg2.Error as e:
        print(e)
    else:
        cursor = conn.cursor()
        #sql_delete = "select * from employee where id = %s;"
        sql_show = "select * from employee;"
        cursor.execute(sql_show)
        rs = cursor.fetchall() #storing the fetched data
        for row in rs:
            print(f"{row[0]}\t{row[1]}\t{row[2]}") #printing the content of the table


        cursor.close()



#getConnection()
#create_table()
#insert_data()
#delete_data()
#update_data()
view_data()