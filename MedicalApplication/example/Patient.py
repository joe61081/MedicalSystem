from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import jsonpickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/medicalreports'
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = "alc_Patients"
    patient_id = db.Column(db.Integer,primary_key=True) 
    patient_name = db.Column('patient_name',db.String(20))
    patient_date_of_birth = db.Column('patient_date_of_birth',db.String(30))
    patient_location = db.Column('patient_location',db.String(30))
    patient_occupation = db.Column('patient_occupation',db.String(30))
    
    def __init__(self,params):
        self.patient_name = params["patient_name"]
        self.patient_date_of_birth=params["patient_date_of_birth"]
        self.patient_location=params["patient_location"]
        self.patient_occupation=params["patient_occupation"]
        
    def __str__(self):
        return "Patient Id:"+str(self.patient_id)+"Name:"+self.patient_name+"D.O.B:"+self.patient_date_of_birth+"Location:"+self.patient_date_of_birth+"Occupation:"+self.patient_occupation
    


@app.route("/patient/create")
def create_Patient():
    p = Patient({"patient_name":"dave","patient_date_of_birth":"19/03/1997","patient_location":"Leeds","patient_occupation":"driver"})
    db.session.add(p)
    db.session.commit()
    
    for p in Patient.query.all(): 
        print("Patient Id:"+str(p.patient_id)+"Name:"+p.patient_name+"D.O.B:"+p.patient_date_of_birth+"Location:"+p.patient_date_of_birth+"Occupation:"+p.patient_occupation)
     
@app.route("/patient/example")
def fetch_all_Patient():
    
    patients = Patient.query.all()
    
    for p in patients: 
        print("Patient Id:"+str(p.patient_id)+"Name:"+p.patient_name+"D.O.B:"+p.patient_date_of_birth+"Location:"+p.patient_date_of_birth+"Occupation:"+p.patient_occupation)
        
    return jsonpickle.encode(patients)    
     
    
if __name__ == '__main__':
    db.create_all()
    create_Patient()
    app.run(port=7700)
    pass