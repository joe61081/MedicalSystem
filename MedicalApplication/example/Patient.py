from flask.app import Flask, request, Response
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
from flask.templating import render_template
from _datetime import datetime
<<<<<<< HEAD
from flask.globals import request
=======
from flask.globals import request, session


>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/medicalreports'
db = SQLAlchemy(app)

#Classes
class Patient(db.Model):
    __tablename__ = "alc_Patients"
    patient_id = db.Column(db.Integer,primary_key=True) 
    patient_name = db.Column('patient_name',db.String(20))
    patient_date_of_birth = db.Column('patient_date_of_birth',db.String(30))
    patient_location = db.Column('patient_location',db.String(30))
    patient_occupation = db.Column('patient_occupation',db.String(30))
<<<<<<< HEAD
    #manager_id = db.Column(db.Integer,db.ForeignKey('alc_managers.manager_id'),nullable=False)
    #report_id =db.Column(db.Integer,db.ForeginKey('alc_report.report_id'),nullable=False)
=======
    #manager_id = db.Column(db.Integer,db.ForeignKey('alc_Managers.manager_id'),nullable=False)
    #reports = db.relationship("Report", backref=db.backref('Patients', lazy=True))
    
    
    
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
    def __init__(self,params):
        self.patient_name = params["patient_name"]
        self.patient_date_of_birth=params["patient_date_of_birth"]
        self.patient_location=params["patient_location"]
        self.patient_occupation=params["patient_occupation"]
<<<<<<< HEAD
        pass
=======
       
        
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
    def __str__(self):
        return "Patient Id:"+str(self.patient_id)+"Name:"+self.patient_name+"D.O.B:"+self.patient_date_of_birth+"Location:"+self.patient_date_of_birth+"Occupation:"+self.patient_occupation
<<<<<<< HEAD
class Report(db.Model):
    __tablename__ = "alc_reports"
    report_id = db.Column(db.Integer,primary_key=True)
    condition = db.Column('condition',db.String(50))
    date = db.Column('date', db.TIMESTAMP, nullable=False)
    #patients = db.relationship('Patient',backref=db.backref('report',lazy=True))
    def __init__(self,params):
        self.condition = params["condition"]
        self.date = params["date"]
        pass
    
    def __str__(self):
        return "Id:"+str(self.report_id)+" condition:"+self.condition+ "date:"+str(self.date) 
class Manager(db.Model):
    __tablename__ = "alc_Managers"
    manager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column('manager_name', db.String(50))
    #patients =db.relationship('Patient',backref=db.backref('manager',lazy=True))
    
    def __init__(self, params):
        self.name = params["name"]
    pass
    def __str__(self):
        return "Id: "+str(self.manager_id)+" Name: "+self.name    
 
# Create Methods
@app.route("/patient/create")
=======
    



@app.route('/patient/create', methods = ['POST'])
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
def create_Patient():
   # p = Patient({"patient_name":"dave","patient_date_of_birth":"19/03/1997","patient_location":"Leeds","patient_occupation":"driver"})
    db.session.add(
        Patient({
            "patient_name": request.form.get('patient_name'),
            "patient_date_of_birth": request.form.get('patient_date_of_birth'),
            "patient_location": request.form.get('patient_location'),
            "patient_occupation": request.form.get('patient_occupation'),}))
    db.session.commit()
    patients = Patient.query.all()
    for p in patients: 
        print("Patient Id:"+str(p.patient_id)+"Name:"+p.patient_name+"D.O.B:"+p.patient_date_of_birth+"Location:"+p.patient_date_of_birth+"Occupation:"+p.patient_occupation)
<<<<<<< HEAD
=======
    
    return jsonpickle.encode(patients) 
@app.route("/patient/example")
def fetch_all_Patient():
    
    patients = Patient.query.all()
    
    for p in patients: 
        print("Patient Id:"+str(p.patient_id)+"Name:"+p.patient_name+"D.O.B:"+p.patient_date_of_birth+"Location:"+p.patient_date_of_birth+"Occupation:"+p.patient_occupation)
        
    return jsonpickle.encode(patients)    
   
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git

<<<<<<< HEAD
@app.route("/api/insert-patient", methods = ['POST'])
def insert_Patient():
    db.session.add(
        Patient({
            "patient_name": request.form.get('patient_name'),
            "patient_date_of_birth":request.form.get('patient_date_of_birth'),
            "patient_location":request.form.get('patient_location'),
            "patient_occupation":request.form.get('patient_occupation')
             }))
    db.session.commit()
    

=======
class Manager(db.Model):
    __tablename__ = "alc_Managers"
    manager_id = db.Column(db.Integer, primary_key=True)
    name = db.Column('manager_name', db.String(50))
    '''patients= db.relationship('Patient',
                              backref=db.backref('Manager', lazy=True))
    '''
    def __init__(self, params):
        self.name = params["name"]
    
    def __str__(self):
        return "Id: "+str(self.manager_id)+" Name: "+self.name
   
>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git

@app.route("/manager-create")
def create_manager():
    man = Manager({"name":"Test Manager 3"})
    
    db.session.add(man)
    db.session.commit()
    
    for man in Manager.query.all():
        print("ID: "+str(man.manager_id)+" Name: "+man.name )
    
    return jsonpickle.encode(Manager.query.all())
<<<<<<< HEAD
  
=======

@app.route("/manager-fetch")
def fetch_all_managers():
    managers = Manager.query.all()
    
    for man in managers:
        print("ID: "+str(man.manager_id)+" Name: "+man.name)
        
    return jsonpickle.encode(managers)

def getTimestamp():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Report(db.Model):
    __tablename__ = "alc_reports"
    report_id = db.Column(db.Integer,primary_key=True)
    condition = db.Column('condition',db.String(50))
    date = db.Column('date', db.TIMESTAMP, nullable=False)
    #patient_id = db.Column("Patient", db.Integer, db.ForeignKey('alc_Patients.patient_id'), nullable=False)
    
    def __init__(self,params):
        self.condition = params["condition"]
        self.date = params["date"]
        #self.patient_id = params["Patients"]
        pass
    
    def __str__(self):
        return "Id:"+str(self.report_id)+" condition:"+self.condition+ "date:"+str(self.date)

>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
@app.route("/report-create")
def create_report():
    rep = Report({"condition":"cough","date":getTimestamp()}) 
    
    db.session.add(rep)
    db.session.commit()  
    for rep in Report.query.all():

        print("ID: "+str(rep.report_id)+" condition: "+(rep.condition)+" date: "+str(rep.date) )

        print("ID: "+str(rep.report_id)+" condition: "+(rep.condition)+" date: "+str(rep.date))

    
    return str(Report.query.all())

#Fetch Methods
@app.route("/patient/example")
def fetch_all_Patient():
    
    patients = Patient.query.all()
    
    for p in patients: 
        print("Patient Id:"+str(p.patient_id)+"Name:"+p.patient_name+"D.O.B:"+p.patient_date_of_birth+"Location:"+p.patient_date_of_birth+"Occupation:"+p.patient_occupation)
    return jsonpickle.encode(patients)   
@app.route("/manager-fetch")
def fetch_all_managers():
    managers = Manager.query.all()
    for man in managers:
        print("ID: "+str(man.manager_id)+" Name: "+man.name)  
    return jsonpickle.encode(managers)
def getTimestamp():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
@app.route("/report-fetch")
def fetch_all_reports():
    reports = Report.query.all()
    
    for rep in reports:
        print("ID: "+str(rep.report_id)+" condition: "+(rep.condition)+" date: "+rep.date)        
    return jsonpickle.encode(reports)

if __name__ == '__main__':
<<<<<<< HEAD
    db.create_all()
    create_Patient()
    create_manager()
    create_report()
    
=======
    db.create_all()

    #db.create_all()
    #create_manager()
    #create_report()
    #create_Patient()

>>>>>>> branch 'master' of https://github.com/joe61081/MedicalSystem.git
    app.run(port=7700)
    pass