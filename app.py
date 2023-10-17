from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

list=[]
@app.route("/create")
def helloworld():  
    
    list.append(product)
    return render_template("index.html",data=list)





@app.route("/", methods=["post","get"])
def createdata():
 if request.method=="POST":
    productcode=request.form.get("productcode")
    name=request.form.get("name")
    price=request.form.get("price")
    url=request.form.get("url")
    product=productDetail(productcode,name,price,url)
    list.append(product)
    return redirect(url_for('helloworld'))

 return render_template("create.html",data=list)

class productDetail:
    def __init__(self,productcode,name,price,url):
        self.productcode=productcode
        self.name=name
        self.price=price
        self.url=url

    # def marks(mark1,mark2,mark3,mark4):
    #     p=mark1+mark2+mark3+mark4
    #     return(p)

    def userdata(self):
        return self.productcode,self.name,self.price,self.url
        # print(self.productcode,self.name,self.price,self.url)

product = productDetail("MRON-1758","Microwave-Oven",17500,"./static/images/oven.jpg")


# product = productDetail(nam","name",17500,"./static/images/oven.jpg")


if __name__=="__main__":
    app.run(debug=True)



