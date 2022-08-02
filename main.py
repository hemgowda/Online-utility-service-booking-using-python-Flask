import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
from form import ContactForm
import requests
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'db': 'utility',
'host': 'localhost',
'port': 27017
}
db = MongoEngine()
db.init_app(app)


class utility(db.Document):
    billers = db.StringField()
    customer_id = db.StringField()
    payment_method=db.StringField()
    billing_type=db.StringField()
    billing_cost =db.IntField()
  
    def to_json(self):
        return {"billers": self.billers,
                "customer_id": self.customer_id,
                "payment_method":self.payment_method,
                'billing_type':self.billing_type,
                'billing_cost':self.billing_cost,
                }


@app.route('/', methods=['POST'])
def create_record():
 
 record = json.loads(request.data)
 c = utility(billers=record['billers'],
            customer_id=record['customer_id'],
            payment_method=record['payment_method'],
            billing_type=record['billing_type'],
            billing_cost=record['billing_cost'],)
 c.save()
 return jsonify(c.to_json())

@app.route('/add',methods=['GET','POST'])
def add():
 form = ContactForm()  
 if request.method=="GET":
   return render_template("add.html",form=form)
 else:
      x={
            "billers":request.form['billers'],
            "customer_id":request.form['customer_id'],
            "payment_method":request.form['payment_method'],
            "billing_type":request.form['billing_type'],
            "billing_cost":request.form['billing_cost'],
   
         }
      
      y=json.dumps(x)
    
      response = requests.post(url="http://127.0.0.1:5000/",data=y)
      #loaded_json = json.loads(x)
      
      return render_template('x.html',a=x)
 
if __name__ == '__main__': 
 app.run(debug = True)
 