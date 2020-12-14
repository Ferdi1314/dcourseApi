from pymongo import MongoClient
from pprint import pprint
import json
from bson import json_util

class Database():
    def __init__(self):
        client = MongoClient("mongodb+srv://ferdinand:1234@pinjamruang.uvym6.mongodb.net/PinjamRuang?retryWrites=true&w=majority")
        self.Account=client.dcourse.account
        self.Content=client.dcourse.content
        self.Course=client.dcourse.course

#######################ACCOUNT#######################    
    def addAcc(self,data):
        self.Account.insert_one(data)
        return("Account added")
    
    def listAcc(self):
        listing = self.Account.find()
        elist = []
        for c in listing:
            tempa = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id'):
                    tempa[k] = c[k]
            elist.append(tempa)
        print(elist)
        return(elist)

    def findAcc(self,data):
        listing = self.Account.find(data)
        elist = []
        for c in listing:
            tempa = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id'):
                    tempa[k] = c[k]
            elist.append(tempa)
        print(elist)
        return(elist)

    def updateAcc(self,username,data):
        update_data = {}
        for key in data.keys():
            if data[key] != None:
                update_data[key] = data [key]
        self.Account.update_one({"username": username}, {"$set": update_data})
        return("Account updated")
    
    def delAcc(self,data):
        self.Account.delete_one(data)
        return("Account deleted")