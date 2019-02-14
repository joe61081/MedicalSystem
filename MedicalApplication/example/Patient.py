from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
from flask.templating import render_template
from _datetime import datetime

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
    #manager_id = db.Column(db.Integer,db.ForeignKey('alc_managers.manager_id'),nullable=False)
    
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
   

class Manager(db.Model):
    __tablename__ = "alc_Managers"
    manager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column('manager_name', db.String(50))
    
    def __init__(self, params):
        self.name = params["name"]
    
    def __str__(self):
        return "Id: "+str(self.manager_id)+" Name: "+self.name
   

@app.route("/manager-create")
def create_manager():
    man = Manager({"name":"Test Manager 3"})
    
    db.session.add(man)
    db.session.commit()
    
    for man in Manager.query.all():
        print("ID: "+str(man.manager_id)+" Name: "+man.name )
    
    return jsonpickle.encode(Manager.query.all())

@app.route("/manager-fetch")
def fetch_all_managers():
    managers = Manager.query.all()
    
    for man in managers:
        print("ID: "+str(man.manager_id)+" Name: "+man.name)
        
    return jsonpickle.encode(managers)


def getTimestamp():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Report(db.Model):
    __tablename__ = "med_patients"
    report_id = db.Column(db.Integer,primary_key=True)
    condition = db.Column('condition',db.String(50))
    date = db.Column('date', db.TIMESTAMP, nullable=False)
    
    def __init__(self,params):
        self.condition = params["condition"]
        self.date = params["date"]
        pass
    
    def __str__(self):
        return "Id:"+str(self.report_id)+" condition:"+self.condition+ "date:"+str(self.date)

@app.route("/report-create")
def create_report():
    rep = Report({"condition":"cough","date":getTimestamp()})
    
    db.session.add(rep)
    db.session.commit()
    
    for rep in Report.query.all():
        print("ID: "+str(rep.report_id)+" condition: "+(rep.condition)+" date: "+rep.date )
    
    return str(Report.query.all())

@app.route("/report-fetch")
def fetch_all_reports():
    reports = Report.query.all()
    
    for rep in reports:
        print("ID: "+str(rep.report_id)+" condition: "+(rep.condition)+" date: "+rep.date)
        
    return jsonpickle.encode(reports)




if __name__ == '__main__':
    #db.create_all()
    create_Patient()
    create_manager()
    create_report()
    
    app.run(port=7700)
    pass