from flask import Flask,render_template
from model.objects.objects import *

app = Flask(__name__)

@app.route("/")
def start():
    return "welcome to ecom-api"


@app.route("/signup/<string:name>/<string:password>/<string:email>")
def csignup(name,password,email):
    us  = user(name,email,password)
    print(us.userispresent())
    if us.userispresent()=="yes":
        return "/login/your name/ password"
    if us.userispresent() =="no":
        rs = us.addusertodb()
        if rs !=None:
            return "done"
        else:
            return "error"


@app.route("/login/<string:name>/<string:password>/<string:email>")
def clogin(name,password,email):
    us  = user(name,email,password)
    if us.userispresent()=="no":
        return "/signup/your name/ password"
    if us.userispresent() =="yes":
        obj  = us.getuserbynameandpassword()
        ans ={
            "name":obj["name"],
            "password":obj["password"],
            "email":obj["email"],
            "history":obj["bhistory"],
            "tobuy" :"/buy/model_no/name/password/email"
            }
        return ans

@app.route("/admin/signup/<string:name>/<string:password>/<string:email>")
def asignup(name,password,email):
    us  = admin(password,name,email)
    print(us.adminispresent())
    if us.adminispresent()==True:
        return "/login/your name/ password"
    if us.adminispresent() ==False:
        rs = us.addadmintodb()
        if rs !=None:
            return "done"
        else:
            return "error"


@app.route("/admin/login/<string:name>/<string:password>/<string:email>")
def alogin(name,password,email):
    us  = admin(password,name,email)
    print(us.adminispresent())
    if us.adminispresent()==True:
        obj = us.getadminbynameandpassword()
        ans ={
            "name":obj["name"],
            "password":obj["password"],
            "email":obj["email"],
            "sellhistory":obj["shistory"],
            "listed-products":obj["lproduct"],
            "tolist" :"/list/model_no/name/password/email",
            "total-earning-today": us.totalproductsoldtoday(),
            "total-investment-left":us.toltalproductleft(),
            "total-earning-tilldate":us.totalproductsold()
            }
        print(us.totalproductsold())
        return ans
    if us.adminispresent() ==False:
        return "not present"

@app.route("/admin/<string:name>/<string:password>/<string:email>/<string:model>/<string:mname>/<string:price>/list")
def list(name,password,email,model,mname,price):
    us  = admin(password,name,email)
    pr = product(int(price),mname,model,name)
    pr.addproducttodb()
    ins_id = us.updateadminlistedproduct(pr)
    pr.addproducttodb()
    print(int(price))
    return "ok"
    # return int(price)

@app.route("/admin/<string:name>/<string:password>/<string:model>/<string:pname>/<string:price>/buy/<string:uname>/<string:upas>")
def buy(name,password,model,pname,price,uname,upas):
    us =user(uname,"",upas)
    ad  =admin(password,name,"")
    pr =product(price,pname,model,name)
    us.updateuser(pr)
    ad.updateadminsell(pr)
    pr.deleteproduct()
    return "ol"


if __name__ == "__main__":
    app.run(debug=True)
