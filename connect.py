
import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kiki1979!",
    database="BUTCHERSHOP"
)
 
# Creating an instance of 'cursor' class 
# which is used to execute the 'SQL' 
# statements in 'Python'
cursor = mydb.cursor()
 
# Creating a database with a name
# 'geeksforgeeks' execute() method 
# is used to compile a SQL statement
# below statement is used to create 
# the 'geeksforgeeks' database
# cursor.execute("CREATE DATABASE butchershop")
# cursor.execute("CREATE TABLE Payment (purchaseID INT, lastFourDigits VARCHAR(4), lastNameOnCard VARCHAR(255), total DECIMAL)")
# cursor.execute("CREATE TABLE Meat ( meatID INT, typeOfMeat VARCHAR(30), pricePerPound DECIMAL, lbsRemaining R DECIMAL)")

addMeat = "INSERT INTO Meat (meatID, typeOfMeat, pricePerPound, lbsRemaining) values (%d,%s,%d,%d)"
meats = [
    (1, "Chicken", 10.99, 430),
    (2, "Pork", 9.40, 60),
    (3, "Salmon", 15.93, 90),
    (4, "Beef", 8.99, 100)
]

for meat in meats:
    cursor.execute(addMeat, meats)
#cursor.execute("INSERT INTO Meat () VALUES (%s, %s)")