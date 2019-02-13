from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from _datetime import datetime
import jsonpickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medicalreports'
db = SQLAlchemy(app)

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
    db.create_all() #create the schema using the alchemy context
    create_report()
    
    app.run(port=7700)
    pass
    
    