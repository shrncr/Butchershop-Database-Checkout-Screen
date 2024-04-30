'''
Queries associated w the butchershop
'''
#sEFIMejPDjpLxs4B
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://shrncr:qd2WizrbtswCc6Z1@cluster0.qdbsdrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["activity5"]
meat_collection = db["Meat"]
cart_collection = db["cart"]
payment_collection = db["Payment"]
def query(type, data=None):
    if type == "getMeat":
        # Get available meat in the butchershop
        meats = meat_collection.find({"lbsRemaining": {"$gt": 0}}, {"typeOfMeat": 1, "pricePerPound": 1, "lbsRemaining": 1})
        return list(meats)

    if type == "specMeat":
        meat = meat_collection.find_one({"typeOfMeat": data[0]}, {"typeOfMeat": 1, "pricePerPound": 1, "lbsRemaining": 1})
        return meat

    elif type == "addToCart":
        # Add entry to cart collection
        cart_collection.insert_one({
            "cartID": data[0],
            "transactionID": data[1],
            "typeOfMeat": data[2],
            "weight": data[3],
            "purchaseID": data[4],
            "meatID": data[5]
        })

    elif type == "purchase":
        # Add to payment collection
        payment_collection.insert_one({
            "purchaseID": data[0],
            "lastFourDigits": str(data[1]),
            "lastNameOnCard": data[2],
            "total": data[3]
        })

        # Update lbsRemaining in Meat collection
        for meat, weight in data[4].items():
            meat_collection.update_one({"typeOfMeat": meat}, {"$inc": {"lbsRemaining": -weight}})

    elif type == "getCart":
        # Get items added to the cart
        cart = cart_collection.find({"transactionID": {"$regex": data}}, {"_id": 0})
        newList = []
        for item in cart:
            meat = meat_collection.find_one({"typeOfMeat": item["typeOfMeat"]}, {"pricePerPound": 1})
            total = meat["pricePerPound"] * item["weight"]
            newEntry = {**item, "total": total}
            newList.append(newEntry)
        return newList



#import mysql.connector
# def query(type, data=None): #data param only input if it is update/insert     
#     mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "Kiki1979!",
#         database = "BUTCHERSHOP"
#     )
#     cursor = mydb.cursor()

#     if type=="getMeat": #get available meat in the butchershop
#         cursor.execute("SELECT typeOfMeat,pricePerPound,lbsRemaining from Meat WHERE lbsRemaining>0")
#         meats = cursor.fetchall()
#         return meats
#     if type=="specMeat":
#         sql = ("SELECT typeOfMeat,pricePerPound,lbsRemaining from Meat WHERE typeOfMeat = %s")
#         val = [data[0]]
#         cursor.execute(sql,val)
#         meat = cursor.fetchall()
#         return meat

#     elif type == "addToCart": #adds entry to cart table when user taps "sumbit" button in purchasePromptGUI
#         sql = "INSERT INTO cart (cartID,transactionID, typeOfMeat, weight, purchaseID, meatID) VALUES (%s, %s,%s,%s,%s,%s )"
#         val = (data[0], data[1], data[2],data[3],data[4],data[5])
#         cursor.execute(sql, val)
#         mydb.commit()
        
#     elif type=="purchase": #adds to purchase table when a user fully checks out in checkoutGUI
#         sql = "INSERT INTO Payment (purchaseID, lastFourDigits, lastNameOnCard, total) VALUES (%s, %s, %s, %s)"
#         val = (data[0], str(data[1]), data[2], data[3])
#         print("Attempting to insert:", val)
#         cursor.execute(sql, val)
#         print(data[4])
#         for meat in data[4]:
#             print(meat + "meat")
#             print(data[4][meat])
#             sql = "UPDATE Meat SET lbsRemaining=lbsRemaining-%s WHERE typeOfMeat =%s"
#             values = (data[4][meat],meat)#decreases meats(key) by #lbs purchased (val)
#             cursor.execute(sql, values)
#         print("thanks.")
#         #note: doesnt work bc it will have to decrease each meat which was purchased
#         #probs have to use a for loop to make sure we get rid of each meat. idk. we have a whole week left to do this.

#         mydb.commit()
#     elif type=="getCart":#gets items you added to the cart just now
#         cursor.execute("SELECT * FROM cart WHERE transactionID LIKE %s", ([data + "%"]))
#         cart = cursor.fetchall()
#         newList = []
#         for item in cart:
#             cursor.execute("SELECT pricePerPound FROM Meat WHERE typeOfMeat = %s", ([item[2]])) #we have to figure out how much money worth of each meat was added
#             costs = cursor.fetchall() #price per pound
#             total = int(costs[0][0])*int(item[3]) #total aka p/lbXpounds
#             newEntry = [item, total] #an array containing 2 elements: the original tuple, and the total cost of this cart item. sigh.
#              #turn into tuple
#             newList.append(newEntry)
#         return newList
    

