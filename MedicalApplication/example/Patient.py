from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medicalreports'
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = "med_patients"
    patient_id = db.Column(db.Integer,primary_key=True)
    
    name = db.Column('product_name',db.String(50))
    unit_price = db.Column(db.Float)
