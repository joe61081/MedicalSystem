from  flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
import jsonpickle

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medicalreports'

db = SQLAlchemy(app)

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

if __name__ == '__main__':
    db.create_all() #create the schema using the alchemy context
    #example_product()
    #example_payment()
    app.run(port=7700)
    pass
    