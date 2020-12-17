import time as tm
import pymongo

from pymongo.mongo_client import *

from pymongo.read_preferences import Primary


client = MongoClient('localhost',27017)

db = client.ecom

coll = db.userdb

colld =db.productdb

colla = db.admindb

def prodtodict(p):
    dictprod = {
                    "name" : p.name,
                    "price":p.price,
                    "model":p.model,
                    "soldby":p.soldby,
                    "soldon":p.soldon,
                }
    return dictprod
class user:

    def __init__(self,name,email,password):
        self.email  =email
        self.password =password
        self.name=name
        self.buyinghistory =[]
    
    def addproduct(self,p):
        prod = prodtodict(p)
        self.buyinghistory.append(prod)
        return self.buyinghistory

    def removeproduct(self,p):
        for val in self.buyinghistory:
            if val.name == p.name:
                self.buyinghistory.pop(val)
            else:
                print("you havent bought that product")

    def addusertodb(self):
        data = {"name":self.name,"email":self.email,"password":self.password,"bhistory":self.buyinghistory}
        mdata=coll.insert_one(data)
        return (mdata.inserted_id)
    
    def userispresent(self):
        res = "no"
        user = {
                "name":self.name,
                "password":self.password,
                # "email":self.email,
                # "bhistory":self.buyinghistory
            }
        for tst in coll.find():
            if tst["name"] == user["name"]  and user["password"] == tst["password"]:
                res= "yes"
            else:
                continue
        return res
            
    def getuserbynameandpassword(self):
        res = "oof not present"
        userdata = coll.find_one({"name":self.name,"password":self.password})
        if userdata!=None:
            res =  userdata
        return res

    def getalluser(self):
        ar =[]
        for us in coll.find():
            ar.append(us)
        return(ar)

    def updateuser(self,ar):
        ard = prodtodict(ar)
        userdata = coll.find_one({"name":self.name,"password":self.password})
        userdata["bhistory"].append(ar)
        query ={"name":self.name,"password":self.password}
        coll.delete_one(query)
        mdata = coll.insert_one(userdata)
        return mdata.inserted_id
    def deleteuser(self):
        query ={"name":self.name,"password":self.password}
        res = coll.delete_one(query)
        print(res.deleted_count)



class product:
    def __init__(self,price,name,model,soldby):
        date = []
        date.append(tm.localtime().tm_mday)
        date.append(tm.localtime().tm_mon)
        date.append(tm.localtime().tm_year)
        self.price =price
        self.name =name
        self.model =model
        self.soldby = soldby
        self.soldon =date

    def addproducttodb(self):
        data = {"name":self.name,"model":self.model,"price":self.price,"soldby":self.soldby,"soldon":self.soldon}
        mdata=colld.insert_one(data)
        return (mdata.inserted_id)
    
    def productispresent(self):
        res = False
        productdata = {
                        "name":self.name,
                        "model":self.model,
                        "price":self.price,
                        "soldby":self.soldby,
                        "soldon":self.soldon
                        }
        for tst in coll.find():
            if tst["name"] == productdata["name"]  and productdata["model"] == tst["model"]:
                res =True
        return res
            
    def getproductbymodel(self):
        res = "oof not present"
        productdata = colld.find_one({"model":self.model})
        if productdata!=None:
            res =  productdata
        return res

    def getallproduct(self):
        ar =[]
        for us in colld.find():
            ar.append(us)
        return(ar)

    def updateproduct(self,ar):
        productdata = colld.find_one(
                                {
                                "name":self.name,
                                "model":self.model
                                })
        productdata["price"] = ar
        query ={"name":self.name,"model":self.model}
        colld.delete_one(query)
        mdata = colld.insert_one(productdata)
        return mdata.inserted_id

    def deleteproduct(self):
        query ={"model":self.model}
        colld.delete_one(query)
        
def deleteasetproduct(ar):
    for mod in ar:
        query = {"model":mod}
        colld.delete_one(query)


class admin:
    def __init__(self,password,name,email) -> None:
        self.email =email
        self.password=password
        self.name =name
        self.sellinghistory = []
        self.listedproduct =[]
    def addproduct(self,prod:product):
        """
        docstring
        """
        res = []
        dictprod =prodtodict(prod)
        self.sellinghistory.append(dictprod)
        # self.listedproduct.pop(dictprod)
        res.append(self.listedproduct)
        res.append(self.sellinghistory)
        return res

    def addproducttosale(self,prod:product):
        """
        docstring
        """
        dictprod = prodtodict(product)
        self.listedproduct.append(dictprod)
        return self.listedproduct

    def addadmintodb(self):
        data = {
                "name":self.name,
                "password":self.password,
                "email":self.email,
                "shistory":self.sellinghistory ,
                "lproduct":self.listedproduct
                }
        mdata=colla.insert_one(data)
        return (mdata.inserted_id)
    
    def adminispresent(self):
        res = False
        user = {
                "name":self.name,
                "password":self.password,
                "email":self.email,
                "shistory":self.sellinghistory,
                "lproduct":self.listedproduct
                }
        for tst in coll.find():
            if tst["name"] == user["name"] :
                res =True
        return res
            
    def getadminbynameandpassword(self):
        res = "oof not present"
        productdata = colla.find_one({"name":self.name,"password":self.password})
        if productdata!=None:
            res =  productdata
        return res

    def getalladmin(self):
        ar =[]
        for us in colla.find():
            ar.append(us)
        return(ar)

    def updateadminpassword(self,ar):
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })
        admindata["password"] = ar
        query ={"name":self.name,"password":self.password}
        colla.delete_one(query)
        mdata = colla.insert_one(admindata)
        return mdata.inserted_id
    
    def updateadminlistedproduct(self,ar):
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })
        admindata["lproduct"].append(prodtodict(ar))
        query ={"name":self.name,"password":self.password}
        colla.delete_one(query)
        mdata = colla.insert_one(admindata)
        return mdata.inserted_id

    def updateadminsell(self,ar):

        ard = prodtodict(ar)
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })
        admindata["shistory"].append(ard)
        for val in admindata["lproduct"]:
            if val["model"] ==ard["model"]:
                admindata["lproduct"].remove(val)
        query ={"name":self.name,"password":self.password}
        colla.delete_one(query)
        mdata = colla.insert_one(admindata)
        return mdata.inserted_id

    def dropadmin(self):
        query ={"name":self.name,"password":self.password}
        colla.delete_one(query)

    def totalproductsoldtoday(self):
        """ 
        docstring
        """
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })  
        earn = 0
        today = tm.localtime().tm_mday
        for val in admindata["shistory"]:
            if today == val["soldon"][0]:
                earn += int(val["price"])
        return earn
    def totalproductsold(self):
        """
        docstring
        """ 
        earn = 0
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })
        for val in admindata["shistory"]:
            earn += int(val["price"])
        return earn
    def toltalproductleft(self):
        invest = 0
        admindata = colla.find_one(
                                {
                                "name":self.name,
                                "password":self.password
                                })
        for val in admindata["shistory"]:
            invest +=int(val["price"])
        return invest

pr = admin("rishi1709","rishi","")

print(pr.totalproductsoldtoday())