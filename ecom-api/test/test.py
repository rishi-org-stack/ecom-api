
# # from pymongo import *
# import pymongo
# from pymongo.message import query
# from pymongo.mongo_client import *
# from pymongo.read_preferences import Primary
# # from product.product import *

# client = MongoClient('localhost',27017)

# db = client.ecom

# coll = db.userdb

# colld =db.productdb
# class user:
#     def __init__(self,name,email,password):
#         self.email  =email
#         self.password =password
#         self.name=name
#         self.buyinghistory =[]
    
#     def addproduct(self,p):
#         prod = {
#                     "name" : p.name,
#                     "price":p.price,
#                     "model":p.model,
#                     "soldby":p.soldby
#         }
#         self.buyinghistory.append(prod)
#         return self.buyinghistory

#     def removeproduct(self,p):
#         for val in self.buyinghistory:
#             if val.name == p.name:
#                 self.buyinghistory.pop(val)
#             else:
#                 print("you havent bought that product")

#     def addusertodb(self):
#         data = {"name":self.name,"email":self.email,"password":self.password,"bhistory":self.buyinghistory}
#         mdata=coll.insert_one(data)
#         return (mdata.inserted_id)
    
#     def userispresent(self):
#         res = False
#         user = {"name":self.name,
#                 "password":self.password,
#                 "email":self.email,
#                 "bhistory":self.buyinghistory
#             }
#         for tst in coll.find():
#             if tst["name"] == user["name"]  and user["password"] == tst["password"]:
#                 res =True
#         return res
            
#     def getuserbynameandpassword(self):
#         res = "oof not present"
#         userdata = coll.find_one({"name":self.name,"password":self.password})
#         if userdata!=None:
#             res =  userdata
#         return res

#     def getalluser(self):
#         ar =[]
#         for us in coll.find():
#             ar.append(us)
#         return(ar)
#     def updateuser(self,ar):
#         userdata = coll.find_one({"name":self.name,"password":self.password})
#         userdata["bhistory"] = ar
#         query ={"name":self.name,"password":self.password}
#         coll.delete_one(query)
#         mdata = coll.insert_one(userdata)
#         return mdata.inserted_id
#     def deleteuser(self):
#         query ={"name":self.name,"password":self.password}
#         coll.delete_one(query)



# class product:
#     def __init__(self,price,name,model,soldby):
#         self.price =price
#         self.name =name
#         self.model =model
#         self.soldby = soldby

#     def addproducttodb(self):
#         data = {"name":self.name,"model":self.model,"price":self.price,"soldby":self.soldby}
#         mdata=colld.insert_one(data)
#         return (mdata.inserted_id)
    
#     def productispresent(self):
#         res = False
#         productdata = {"name":self.name,
#                 "model":self.model,
#                 "price":self.price,
#                 "soldby":self.soldby
#             }
#         if productdata in colld.find():
#             res= True
#         return res
            
#     def getproductbymodel(self):
#         res = "oof not present"
#         productdata = colld.find_one({"model":self.model})
#         if productdata!=None:
#             res =  productdata
#         return res

#     def getallproduct(self):
#         ar =[]
#         ar =colld.find()
#         return ar

#     def updateproduct(self,ar):
#        pass

#     def deleteproduct(self):
#         query ={"model":self.model}
#         colld.delete_one(query)
        
# def deleteasetproduct(ar):
#     for mod in ar:
#         query = {"model":mod}
#         colld.delete_one(query)

# us = user("rishi","rishistack","rishijha1709")
# pr = product(80,"somsung","12fsa","aniljha")
# newus = us.addproduct(pr)
# p1 = product(120,"nokia","12ksa","komaljha")
# neus =  us.addproduct(p1)
# # us.deleteuser()
# print(us.getalluser())

def ok(ls):
    ans = 0
    for i in ls:
        if i>0:
            ans+=i
    return ans

print(ok([0,1,-1,2,3,4]))