import mysql.connector as db
from Session13 import Customer


# Database username and password
username = "root"
password = "123456"
host = "127.0.0.1"
database = "gw2024"


connection = db.connect(user=username, password=password, host=host, database=database, port="3306")

print("Connection Created")
print(connection)

customer = Customer()
customer.add_customer_details()


# 2. Create SQL Statement
# sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)
sql_update = "update Customer set name = 'Johnnathon', email = 'john.jj@example.com', age=45 where cid = 1"
# 3. Obtain Cursor -> Perform CRUD Operations with MySQL 
cursor = connection.cursor()

# 4. Execute SQL command
cursor.execute(sql_update)

# 5. Commit the write statement
connection.commit()

print("SQL Statement Exexuted")