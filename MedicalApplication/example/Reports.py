from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medicalreports'
db = SQLAlchemy(app)

class Report(db.Model):
    __tablename__ = "med_patients"
    report_id = db.Column(db.Integer,primary_key=True)
    condition = db.Column('condition',db.String(50))
    date = db.Column('date',db.String(20))
    
def __init__(self,params):
        self.name = params["name"]
        self.unit_price = params["price"]
        pass
    
    def __str__(self):
        return "Id:"+str(self.product_id)+" Name:"+self.name+ "Unit Price:"+str(self.unit_price)
    
    