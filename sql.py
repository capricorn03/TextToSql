import sqlite3

##  connect to the database
connection = sqlite3.connect('student.db')

## Create a cursor object
cursor = connection.cursor()

## Create a table 
table_info = """
CREATE TABLE student (Name varchar(20), Section varchar(5), Marks int);
"""

cursor.execute(table_info)

# Queries to INSERT records. 
cursor.execute('''INSERT INTO student VALUES ('Krish', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO student VALUES ('Darius', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO student VALUES ('Sudhanshu', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO student VALUES ('Vikash', 'Data Science', 'C')''') 

# Dispaly the inserted records
print("The inserted record are..")
data = cursor.execute('''SELECT * FROM student''')

for row  in data:
    print(row)
    
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()