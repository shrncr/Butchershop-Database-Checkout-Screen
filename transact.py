'''
Queries associated w the butchershop
'''
from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("mongodb://localhost:27017/")  
    db = client.BUTCHERSHOP  
    return db

def query(type, data=None):
    db = connect_mongo()
    
    if type == "getMeat":
        meats = list(db.Meat.find({"lbsRemaining": {"$gt": 0}}, {"_id": 0, "typeOfMeat": 1, "pricePerPound": 1, "lbsRemaining": 1}))
        return meats

    elif type == "specMeat":
        meat = list(db.Meat.find({"typeOfMeat": data[0]}, {"_id": 0, "typeOfMeat": 1, "pricePerPound": 1, "lbsRemaining": 1}))
        return meat


    elif type == "addToCart":
        cart = {
            "cartID": data[0],
            "transactionID": data[1],
            "typeOfMeat": data[2],
            "weight": data[3],
            "purchaseID": data[4],
            "meatID": data[5]
        }
        db.cart.insert_one(cart)

        
    elif type == "purchase":
        payment = {
            "purchaseID": data[0],
            "lastFourDigits": data[1],
            "lastNameOnCard": data[2],
            "total": data[3]
        }
        db.Payment.insert_one(payment)
        
        for meat, weight in data[4].items(): # update lbsRemaining 
            db.Meat.update_one({"typeOfMeat": meat}, {"$inc": {"lbsRemaining": -weight}})


    elif type == "getCart":
        cart_items = list(db.cart.find({"transactionID": {"$regex": data + ".*"}}, {"_id": 0}))
        
        newList = []
        for item in cart_items:
            meat_data = db.Meat.find_one({"typeOfMeat": item["typeOfMeat"]}, {"pricePerPound": 1, "_id": 0})
            total = meat_data["pricePerPound"] * item["weight"]
            newList.append((item, total))
        return newList

    

